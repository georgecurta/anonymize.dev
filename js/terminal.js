/**
 * Anonymize.dev - Terminal Animations
 * Interactive terminal typing effects for hero and demo sections
 */

class TerminalTyping {
  constructor(container, options = {}) {
    this.container = container;
    this.options = {
      typeSpeed: 50,
      deleteSpeed: 30,
      lineDelay: 500,
      cursorBlink: true,
      loop: false,
      ...options
    };

    this.lines = [];
    this.currentLine = 0;
    this.isTyping = false;
    this.cursor = null;

    this.init();
  }

  init() {
    // Parse pre-defined lines from data attribute or children
    const linesData = this.container.dataset.lines;
    if (linesData) {
      try {
        this.lines = JSON.parse(linesData);
      } catch (e) {
        console.error('Failed to parse terminal lines:', e);
      }
    }

    // Create cursor
    if (this.options.cursorBlink) {
      this.cursor = document.createElement('span');
      this.cursor.className = 'terminal__cursor';
      this.container.appendChild(this.cursor);
    }
  }

  async start() {
    if (this.isTyping || this.lines.length === 0) return;
    this.isTyping = true;

    for (const line of this.lines) {
      await this.typeLine(line);
      await this.delay(this.options.lineDelay);
    }

    if (this.options.loop) {
      await this.delay(2000);
      this.clear();
      this.start();
    } else {
      this.isTyping = false;
    }
  }

  async typeLine(lineConfig) {
    const lineEl = document.createElement('div');
    lineEl.className = 'terminal__line';

    if (lineConfig.type === 'command') {
      // Command line with prompt
      const promptEl = document.createElement('span');
      promptEl.className = 'terminal__prompt';
      promptEl.textContent = lineConfig.prompt || '$ ';
      lineEl.appendChild(promptEl);

      const commandEl = document.createElement('span');
      commandEl.className = 'terminal__command';
      lineEl.appendChild(commandEl);

      // Insert before cursor
      if (this.cursor) {
        this.container.insertBefore(lineEl, this.cursor);
      } else {
        this.container.appendChild(lineEl);
      }

      // Type the command
      await this.typeText(commandEl, lineConfig.text);

    } else if (lineConfig.type === 'output') {
      // Output line (appears instantly)
      lineEl.className = 'terminal__output';
      lineEl.innerHTML = this.highlightSyntax(lineConfig.text, lineConfig.language);

      if (this.cursor) {
        this.container.insertBefore(lineEl, this.cursor);
      } else {
        this.container.appendChild(lineEl);
      }

      await this.delay(100);

    } else if (lineConfig.type === 'comment') {
      // Comment line
      lineEl.className = 'terminal__comment';
      lineEl.textContent = lineConfig.text;

      if (this.cursor) {
        this.container.insertBefore(lineEl, this.cursor);
      } else {
        this.container.appendChild(lineEl);
      }

      await this.delay(100);
    }
  }

  async typeText(element, text) {
    for (const char of text) {
      element.textContent += char;
      await this.delay(this.options.typeSpeed);
    }
  }

  highlightSyntax(text, language) {
    if (!language) return this.escapeHtml(text);

    // Simple syntax highlighting
    let highlighted = this.escapeHtml(text);

    if (language === 'json') {
      // Strings
      highlighted = highlighted.replace(/"([^"]+)":/g, '<span class="terminal__attr">"$1"</span>:');
      highlighted = highlighted.replace(/: "([^"]+)"/g, ': <span class="terminal__string">"$1"</span>');
      // Booleans and nulls
      highlighted = highlighted.replace(/\b(true|false|null)\b/g, '<span class="terminal__keyword">$1</span>');
    } else if (language === 'bash') {
      // Commands
      highlighted = highlighted.replace(/^(\w+)/gm, '<span class="terminal__keyword">$1</span>');
      // Flags
      highlighted = highlighted.replace(/(\s)(--?\w+)/g, '$1<span class="terminal__attr">$2</span>');
      // Strings
      highlighted = highlighted.replace(/'([^']+)'/g, '<span class="terminal__string">\'$1\'</span>');
      highlighted = highlighted.replace(/"([^"]+)"/g, '<span class="terminal__string">"$1"</span>');
    }

    return highlighted;
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  clear() {
    const lines = this.container.querySelectorAll('.terminal__line, .terminal__output, .terminal__comment');
    lines.forEach(line => line.remove());
    this.currentLine = 0;
  }
}

// =============================================
// DATA FLOW ANIMATION
// =============================================

class DataFlowAnimation {
  constructor(container) {
    this.container = container;
    this.svg = null;
    this.isRunning = false;

    this.init();
  }

  init() {
    this.svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    this.svg.setAttribute('width', '100%');
    this.svg.setAttribute('height', '100%');
    this.svg.style.position = 'absolute';
    this.svg.style.top = '0';
    this.svg.style.left = '0';
    this.svg.style.pointerEvents = 'none';
    this.container.appendChild(this.svg);
  }

  start() {
    if (this.isRunning) return;
    this.isRunning = true;
    this.animate();
  }

  stop() {
    this.isRunning = false;
  }

  animate() {
    if (!this.isRunning) return;

    // Create a data point
    const point = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    point.setAttribute('r', '5');
    point.setAttribute('fill', '#ff3366');
    point.setAttribute('filter', 'url(#glow)');

    // Define path
    const startX = 50;
    const endX = this.container.offsetWidth - 50;
    const y = this.container.offsetHeight / 2;

    point.setAttribute('cx', startX);
    point.setAttribute('cy', y);

    this.svg.appendChild(point);

    // Animate
    const duration = 2000;
    const startTime = Date.now();

    const animatePoint = () => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Ease out
      const eased = 1 - Math.pow(1 - progress, 3);
      const currentX = startX + (endX - startX) * eased;

      point.setAttribute('cx', currentX);

      // Change color at midpoint (when passing through MCP)
      if (progress > 0.4 && progress < 0.6) {
        point.setAttribute('fill', '#00ff41');
      } else if (progress >= 0.6) {
        point.setAttribute('fill', '#00ffff');
      }

      if (progress < 1) {
        requestAnimationFrame(animatePoint);
      } else {
        point.remove();
      }
    };

    animatePoint();

    // Schedule next point
    setTimeout(() => this.animate(), 1000);
  }
}

// =============================================
// HERO TERMINAL DEMO
// =============================================

function initHeroTerminal() {
  const heroTerminal = document.querySelector('.hero-terminal .terminal__body');
  if (!heroTerminal) return;

  const demoLines = [
    { type: 'comment', text: '# Configure MCP Server for Claude Desktop' },
    { type: 'command', prompt: '$ ', text: 'cat ~/.config/claude/claude_desktop_config.json' },
    { type: 'output', text: '{', language: 'json' },
    { type: 'output', text: '  "mcpServers": {', language: 'json' },
    { type: 'output', text: '    "anonymize": {', language: 'json' },
    { type: 'output', text: '      "command": "npx",', language: 'json' },
    { type: 'output', text: '      "args": ["-y", "@anonym-legal/mcp-server"]', language: 'json' },
    { type: 'output', text: '    }', language: 'json' },
    { type: 'output', text: '  }', language: 'json' },
    { type: 'output', text: '}', language: 'json' },
    { type: 'comment', text: '' },
    { type: 'comment', text: '# Your prompts are now automatically protected!' },
  ];

  heroTerminal.dataset.lines = JSON.stringify(demoLines);

  const terminal = new TerminalTyping(heroTerminal, {
    typeSpeed: 30,
    lineDelay: 200
  });

  // Start when terminal is visible
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      setTimeout(() => terminal.start(), 500);
      observer.disconnect();
    }
  });

  observer.observe(heroTerminal);
}

// =============================================
// INITIALIZE
// =============================================

document.addEventListener('DOMContentLoaded', () => {
  initHeroTerminal();

  // Initialize data flow animations
  document.querySelectorAll('.data-flow-animation').forEach(container => {
    const dataFlow = new DataFlowAnimation(container);

    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        dataFlow.start();
      } else {
        dataFlow.stop();
      }
    });

    observer.observe(container);
  });
});

// Export for use in other scripts
window.TerminalTyping = TerminalTyping;
window.DataFlowAnimation = DataFlowAnimation;
