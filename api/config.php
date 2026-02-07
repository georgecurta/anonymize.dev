<?php
/**
 * Anonymize.dev - Configuration Placeholder
 *
 * IMPORTANT: This file is for local development only.
 * Production uses /var/www/config/anonymize-dev-mail.php
 *
 * Never commit real credentials to version control!
 */

// Microsoft Graph API credentials (for email sending)
define('MS_GRAPH_CLIENT_ID', 'your-client-id');
define('MS_GRAPH_CLIENT_SECRET', 'your-client-secret');
define('MS_GRAPH_TENANT_ID', 'your-tenant-id');
define('MS_GRAPH_SENDER_EMAIL', 'noreply@anonymize.solutions');

// Email recipient
define('RECIPIENT_EMAIL', 'contact@example.com');

// reCAPTCHA v3 keys
define('RECAPTCHA_SITE_KEY', '6LcFEFosAAAAAH6zUMF5USUNKGGjr07y97nC5uDr');
define('RECAPTCHA_SECRET_KEY', 'your-secret-key');
