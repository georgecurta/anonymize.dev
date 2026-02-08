<?php
/**
 * Anonymize.dev - Contact Form Handler
 * Uses Microsoft Graph API for email sending with reCAPTCHA v3 protection
 */

// CORS headers
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://anonymize.dev');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Handle preflight
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Only allow POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
    exit;
}

// Load configuration
$configFile = '/var/www/config/anonymize-dev-mail.php';
if (file_exists($configFile)) {
    require_once $configFile;
} else {
    require_once __DIR__ . '/config.php';
}

// Rate limiting
$rateLimitFile = sys_get_temp_dir() . '/anonymize_dev_rate_' . md5($_SERVER['REMOTE_ADDR']);
$rateLimit = 5; // requests per minute
$ratePeriod = 60; // seconds

if (file_exists($rateLimitFile)) {
    $rateData = json_decode(file_get_contents($rateLimitFile), true);
    if (time() - $rateData['start'] < $ratePeriod) {
        if ($rateData['count'] >= $rateLimit) {
            http_response_code(429);
            echo json_encode(['success' => false, 'error' => 'Too many requests. Please wait a minute.']);
            exit;
        }
        $rateData['count']++;
    } else {
        $rateData = ['start' => time(), 'count' => 1];
    }
} else {
    $rateData = ['start' => time(), 'count' => 1];
}
file_put_contents($rateLimitFile, json_encode($rateData));

// Get POST data
$input = json_decode(file_get_contents('php://input'), true);

if (!$input) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid request data']);
    exit;
}

// Validate required fields
$errors = [];

$name = trim($input['name'] ?? '');
$email = trim($input['email'] ?? '');
$company = trim($input['company'] ?? '');
$interest = trim($input['interest'] ?? '');
$message = trim($input['message'] ?? '');
$recaptchaToken = trim($input['recaptcha_token'] ?? '');

if (empty($name)) $errors[] = 'Name is required';
if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'Valid email is required';
if (empty($message)) $errors[] = 'Message is required';

// Spam detection
$spamPatterns = [
    '/\b(viagra|cialis|casino|lottery|winner|crypto|bitcoin)\b/i',
    '/\[url=/i',
    '/<a\s+href/i',
    '/http[s]?:\/\/[^\s]+\s+http[s]?:\/\//i' // Multiple URLs
];

foreach ($spamPatterns as $pattern) {
    if (preg_match($pattern, $message) || preg_match($pattern, $name)) {
        $errors[] = 'Message flagged as spam';
        break;
    }
}

if (!empty($errors)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'errors' => $errors]);
    exit;
}

// Verify reCAPTCHA
if (!empty($recaptchaToken) && defined('RECAPTCHA_SECRET_KEY')) {
    $recaptchaUrl = 'https://www.google.com/recaptcha/api/siteverify';
    $recaptchaData = [
        'secret' => RECAPTCHA_SECRET_KEY,
        'response' => $recaptchaToken,
        'remoteip' => $_SERVER['REMOTE_ADDR']
    ];

    $recaptchaOptions = [
        'http' => [
            'method' => 'POST',
            'header' => 'Content-Type: application/x-www-form-urlencoded',
            'content' => http_build_query($recaptchaData)
        ]
    ];

    $recaptchaContext = stream_context_create($recaptchaOptions);
    $recaptchaResult = @file_get_contents($recaptchaUrl, false, $recaptchaContext);

    if ($recaptchaResult) {
        $recaptchaResponse = json_decode($recaptchaResult, true);
        if (!$recaptchaResponse['success'] || $recaptchaResponse['score'] < 0.5) {
            http_response_code(403);
            echo json_encode(['success' => false, 'error' => 'Security verification failed. Please try again.']);
            exit;
        }
    }
}

// Map interest to readable label
$interestLabels = [
    'sales' => 'Sales Inquiry',
    'mcp' => 'MCP Server Integration',
    'api' => 'API Access',
    'desktop' => 'Desktop App',
    'enterprise' => 'Enterprise Solution',
    'support' => 'Technical Support',
    'other' => 'General Inquiry'
];
$interestLabel = $interestLabels[$interest] ?? 'Not specified';

// Prepare email content
$emailSubject = "[Anonymize.dev] New contact: $interestLabel";
$emailBody = "
<html>
<head>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0f; color: #e5e5e5; padding: 20px; }
.container { max-width: 600px; margin: 0 auto; background: #12121a; border: 1px solid #1e1e2e; border-radius: 8px; padding: 24px; }
h1 { color: #00ffff; font-size: 20px; margin-bottom: 20px; }
.field { margin-bottom: 16px; }
.label { color: #6b7280; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; }
.value { color: #e5e5e5; margin-top: 4px; }
.message { background: #1e1e2e; padding: 16px; border-radius: 4px; margin-top: 20px; }
.footer { margin-top: 24px; padding-top: 16px; border-top: 1px solid #1e1e2e; color: #6b7280; font-size: 12px; }
</style>
</head>
<body>
<div class='container'>
<h1>New Contact Form Submission</h1>

<div class='field'>
<div class='label'>Name</div>
<div class='value'>" . htmlspecialchars($name) . "</div>
</div>

<div class='field'>
<div class='label'>Email</div>
<div class='value'><a href='mailto:" . htmlspecialchars($email) . "' style='color: #00ffff;'>" . htmlspecialchars($email) . "</a></div>
</div>

<div class='field'>
<div class='label'>Company</div>
<div class='value'>" . htmlspecialchars($company ?: 'Not provided') . "</div>
</div>

<div class='field'>
<div class='label'>Interest</div>
<div class='value' style='color: #00ff41;'>" . htmlspecialchars($interestLabel) . "</div>
</div>

<div class='message'>
<div class='label'>Message</div>
<div class='value' style='white-space: pre-wrap;'>" . htmlspecialchars($message) . "</div>
</div>

<div class='footer'>
Sent from anonymize.dev contact form<br>
IP: " . $_SERVER['REMOTE_ADDR'] . "<br>
Time: " . date('Y-m-d H:i:s T') . "
</div>
</div>
</body>
</html>
";

// Send via Microsoft Graph API
if (!defined('MS_GRAPH_CLIENT_ID') || !defined('MS_GRAPH_CLIENT_SECRET') || !defined('MS_GRAPH_TENANT_ID')) {
    error_log('Anonymize.dev: MS Graph credentials not configured');
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Email service not configured']);
    exit;
}

// Get access token
$tokenUrl = 'https://login.microsoftonline.com/' . MS_GRAPH_TENANT_ID . '/oauth2/v2.0/token';
$tokenData = [
    'client_id' => MS_GRAPH_CLIENT_ID,
    'client_secret' => MS_GRAPH_CLIENT_SECRET,
    'scope' => 'https://graph.microsoft.com/.default',
    'grant_type' => 'client_credentials'
];

$tokenOptions = [
    'http' => [
        'method' => 'POST',
        'header' => 'Content-Type: application/x-www-form-urlencoded',
        'content' => http_build_query($tokenData)
    ]
];

$tokenContext = stream_context_create($tokenOptions);
$tokenResult = @file_get_contents($tokenUrl, false, $tokenContext);

if (!$tokenResult) {
    error_log('Anonymize.dev: Failed to get MS Graph token');
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Email service temporarily unavailable']);
    exit;
}

$tokenResponse = json_decode($tokenResult, true);
$accessToken = $tokenResponse['access_token'] ?? null;

if (!$accessToken) {
    error_log('Anonymize.dev: No access token in response');
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Email service authentication failed']);
    exit;
}

// Send email
$sendUrl = 'https://graph.microsoft.com/v1.0/users/' . MS_GRAPH_SENDER_EMAIL . '/sendMail';
$emailPayload = [
    'message' => [
        'subject' => $emailSubject,
        'body' => [
            'contentType' => 'HTML',
            'content' => $emailBody
        ],
        'toRecipients' => [
            ['emailAddress' => ['address' => RECIPIENT_EMAIL]]
        ],
        'replyTo' => [
            ['emailAddress' => ['address' => $email, 'name' => $name]]
        ]
    ],
    'saveToSentItems' => 'false'
];

$sendOptions = [
    'http' => [
        'method' => 'POST',
        'header' => [
            'Authorization: Bearer ' . $accessToken,
            'Content-Type: application/json'
        ],
        'content' => json_encode($emailPayload),
        'ignore_errors' => true
    ]
];

$sendContext = stream_context_create($sendOptions);
$sendResult = @file_get_contents($sendUrl, false, $sendContext);

// Check response
$responseCode = 0;
if (isset($http_response_header)) {
    foreach ($http_response_header as $header) {
        if (preg_match('/^HTTP\/\d\.\d\s+(\d+)/', $header, $matches)) {
            $responseCode = (int)$matches[1];
        }
    }
}

if ($responseCode >= 200 && $responseCode < 300) {
    echo json_encode(['success' => true, 'message' => 'Message sent successfully']);
} else {
    error_log('Anonymize.dev: Failed to send email. Response code: ' . $responseCode);
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Failed to send message. Please try again.']);
}
