/**
 * NIELIT Raspberry Pi Practicals - Interactive Manual Engine
 */

// 40-Pin GPIO Header Definition
const RPI_PINOUT = [
  { pin: 1, name: "3V3 Power", type: "3v3", bcm: null, desc: "3.3V Power Rail (Max 50mA total load)" },
  { pin: 2, name: "5V Power", type: "5v", bcm: null, desc: "5V Power Rail (Direct from USB-C/Supply)" },
  { pin: 3, name: "GPIO 2 (SDA1)", type: "i2c", bcm: 2, desc: "I2C Data line with 1.8kΩ pull-up" },
  { pin: 4, name: "5V Power", type: "5v", bcm: null, desc: "5V Power Rail" },
  { pin: 5, name: "GPIO 3 (SCL1)", type: "i2c", bcm: 3, desc: "I2C Clock line with 1.8kΩ pull-up" },
  { pin: 6, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 7, name: "GPIO 4 (GPCLK0)", type: "gpio", bcm: 4, desc: "General purpose I/O / 1-Wire DHT" },
  { pin: 8, name: "GPIO 14 (TXD0)", type: "uart", bcm: 14, desc: "UART Serial Transmit" },
  { pin: 9, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 10, name: "GPIO 15 (RXD0)", type: "uart", bcm: 15, desc: "UART Serial Receive" },
  { pin: 11, name: "GPIO 17", type: "gpio", bcm: 17, desc: "General purpose digital I/O" },
  { pin: 12, name: "GPIO 18 (PWM0)", type: "gpio", bcm: 18, desc: "Hardware PWM Channel 0" },
  { pin: 13, name: "GPIO 27", type: "gpio", bcm: 27, desc: "General purpose digital I/O" },
  { pin: 14, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 15, name: "GPIO 22", type: "gpio", bcm: 22, desc: "General purpose digital I/O" },
  { pin: 16, name: "GPIO 23", type: "gpio", bcm: 23, desc: "General purpose digital I/O" },
  { pin: 17, name: "3V3 Power", type: "3v3", bcm: null, desc: "3.3V Power Rail" },
  { pin: 18, name: "GPIO 24", type: "gpio", bcm: 24, desc: "General purpose digital I/O" },
  { pin: 19, name: "GPIO 10 (MOSI)", type: "spi", bcm: 10, desc: "SPI0 Master-Out Slave-In" },
  { pin: 20, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 21, name: "GPIO 9 (MISO)", type: "spi", bcm: 9, desc: "SPI0 Master-In Slave-Out" },
  { pin: 22, name: "GPIO 25", type: "gpio", bcm: 25, desc: "General purpose digital I/O" },
  { pin: 23, name: "GPIO 11 (SCLK)", type: "spi", bcm: 11, desc: "SPI0 Clock" },
  { pin: 24, name: "GPIO 8 (CE0)", type: "spi", bcm: 8, desc: "SPI0 Chip Enable 0" },
  { pin: 25, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 26, name: "GPIO 7 (CE1)", type: "spi", bcm: 7, desc: "SPI0 Chip Enable 1" },
  { pin: 27, name: "GPIO 0 (ID_SD)", type: "i2c", bcm: 0, desc: "HAT EEPROM I2C Data (Reserved)" },
  { pin: 28, name: "GPIO 1 (ID_SC)", type: "i2c", bcm: 1, desc: "HAT EEPROM I2C Clock (Reserved)" },
  { pin: 29, name: "GPIO 5", type: "gpio", bcm: 5, desc: "General purpose digital I/O" },
  { pin: 30, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 31, name: "GPIO 6", type: "gpio", bcm: 6, desc: "General purpose digital I/O" },
  { pin: 32, name: "GPIO 12 (PWM0)", type: "gpio", bcm: 12, desc: "Hardware PWM Channel 0" },
  { pin: 33, name: "GPIO 13 (PWM1)", type: "gpio", bcm: 13, desc: "Hardware PWM Channel 1" },
  { pin: 34, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 35, name: "GPIO 19 (MISO1)", type: "spi", bcm: 19, desc: "SPI1 MISO / Hardware PWM1" },
  { pin: 36, name: "GPIO 16", type: "gpio", bcm: 16, desc: "General purpose digital I/O" },
  { pin: 37, name: "GPIO 26", type: "gpio", bcm: 26, desc: "General purpose digital I/O" },
  { pin: 38, name: "GPIO 20 (MOSI1)", type: "spi", bcm: 20, desc: "SPI1 MOSI" },
  { pin: 39, name: "Ground (GND)", type: "gnd", bcm: null, desc: "0V Ground reference" },
  { pin: 40, name: "GPIO 21 (SCLK1)", type: "spi", bcm: 21, desc: "SPI1 SCLK" }
];

// State Management
let currentFilter = "All";
let currentSearch = "";
let highlightedPins = new Set();

document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  renderSidebar();
  renderPinout();
  renderPracticals();
  setupEventListeners();
});

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem("nielit_manual_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute("data-theme") || "dark";
  const newTheme = currentTheme === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", newTheme);
  localStorage.setItem("nielit_manual_theme", newTheme);
  updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
  const btn = document.getElementById("themeToggleBtn");
  if (btn) {
    btn.innerHTML = theme === "dark" ? "☀️" : "🌙";
  }
}

// Sidebar Navigation
function renderSidebar() {
  const container = document.getElementById("sidebarNavList");
  if (!container) return;

  container.innerHTML = PRACTICALS_DATA.map(p => `
    <li>
      <button class="nav-item-btn" onclick="scrollToPractical('${p.id}')">
        <span><strong>${p.num}</strong> ${p.title}</span>
        <span class="nav-badge badge-${p.difficulty.toLowerCase()}">${p.difficulty[0]}</span>
      </button>
    </li>
  `).join("");
}

// Interactive 40-Pin Header
function renderPinout() {
  const board = document.getElementById("pinoutBoard");
  if (!board) return;

  let html = "";
  for (let i = 0; i < RPI_PINOUT.length; i += 2) {
    const left = RPI_PINOUT[i];     // Odd pin (Left)
    const right = RPI_PINOUT[i + 1]; // Even pin (Right)

    html += `
      <div class="pin-row" data-left-pin="${left.pin}" data-right-pin="${right.pin}">
        <div class="pin-label-left" onclick="showPinDetails(${left.pin})" title="${left.desc}">
          ${left.name} (${left.pin})
        </div>
        <div class="pin-header-center">
          <div class="pin-socket bg-${left.type}" id="pin-socket-${left.pin}" 
               data-pin="${left.pin}" data-bcm="${left.bcm}"
               onmouseenter="hoverPin(${left.bcm})" onmouseleave="clearPinHover()"
               onclick="showPinDetails(${left.pin})" title="Pin ${left.pin}: ${left.name}">
            ${left.pin}
          </div>
          <div class="pin-socket bg-${right.type}" id="pin-socket-${right.pin}" 
               data-pin="${right.pin}" data-bcm="${right.bcm}"
               onmouseenter="hoverPin(${right.bcm})" onmouseleave="clearPinHover()"
               onclick="showPinDetails(${right.pin})" title="Pin ${right.pin}: ${right.name}">
            ${right.pin}
          </div>
        </div>
        <div class="pin-label-right" onclick="showPinDetails(${right.pin})" title="${right.desc}">
          (${right.pin}) ${right.name}
        </div>
      </div>
    `;
  }
  board.innerHTML = html;
}

function hoverPin(bcm) {
  if (!bcm) return;
  const matches = PRACTICALS_DATA.filter(p => p.pins.includes(bcm));
  const pinBanner = document.getElementById("pinHoverBanner");
  if (pinBanner) {
    if (matches.length > 0) {
      pinBanner.innerHTML = `<strong>BCM GPIO ${bcm}</strong> is used in: ${matches.map(m => `<code>Practical ${m.num} (${m.title})</code>`).join(", ")}`;
      pinBanner.style.display = "block";
    } else {
      pinBanner.innerHTML = `<strong>BCM GPIO ${bcm}</strong> is currently unassigned in these 20 practicals.`;
      pinBanner.style.display = "block";
    }
  }
}

function clearPinHover() {
  const pinBanner = document.getElementById("pinHoverBanner");
  if (pinBanner && !pinBanner.dataset.locked) {
    pinBanner.style.display = "none";
  }
}

function highlightPracticalPins(pins) {
  // Clear previous
  document.querySelectorAll(".pin-socket").forEach(el => el.classList.remove("highlight"));
  
  pins.forEach(bcm => {
    const pinObj = RPI_PINOUT.find(p => p.bcm === bcm);
    if (pinObj) {
      const el = document.getElementById(`pin-socket-${pinObj.pin}`);
      if (el) el.classList.add("highlight");
    }
  });
}

function showPinDetails(pinNumber) {
  const pinObj = RPI_PINOUT.find(p => p.pin === pinNumber);
  if (!pinObj) return;
  const matches = pinObj.bcm ? PRACTICALS_DATA.filter(p => p.pins.includes(pinObj.bcm)) : [];
  alert(`Pin ${pinObj.pin}: ${pinObj.name}\nType: ${pinObj.type.toUpperCase()}\nDetails: ${pinObj.desc}\nUsed in Practicals: ${matches.length > 0 ? matches.map(m => m.num).join(", ") : "None"}`);
}

// Render Practicals Content
function renderPracticals() {
  const container = document.getElementById("practicalsContainer");
  if (!container) return;

  const filtered = PRACTICALS_DATA.filter(p => {
    const matchesFilter = currentFilter === "All" || p.category === currentFilter || p.difficulty === currentFilter;
    const query = currentSearch.toLowerCase();
    const matchesSearch = !query || 
      p.title.toLowerCase().includes(query) ||
      p.aim.toLowerCase().includes(query) ||
      p.hardware.toLowerCase().includes(query) ||
      p.num.includes(query) ||
      p.code.toLowerCase().includes(query);
    return matchesFilter && matchesSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="hero-card" style="text-align: center;">
        <h3>No practicals matched your search "${currentSearch}"</h3>
        <p style="color: var(--text-muted); margin-top: 0.5rem;">Try searching for "LED", "DHT", "MQTT", "Relay", or "I2C".</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(p => `
    <article class="practical-card" id="practical_${p.id}" onmouseenter="highlightPracticalPins([${p.pins.join(',')}])">
      <div class="card-header">
        <div class="card-title-group">
          <span class="practical-number"># ${p.num}</span>
          <h2 class="card-title">${p.title}</h2>
        </div>
        <div class="card-meta-chips">
          <span class="meta-chip badge-${p.difficulty.toLowerCase()}">${p.difficulty}</span>
          <span class="meta-chip">${p.category}</span>
          <span class="meta-chip">⚡ ${p.hardware}</span>
        </div>
      </div>

      <!-- Tab Navigation -->
      <div class="tabs-header">
        <button class="tab-btn active" onclick="switchTab('${p.id}', 'overview', this)">Overview & Objectives</button>
        <button class="tab-btn" onclick="switchTab('${p.id}', 'wiring', this)">Circuit & GPIO Pinout</button>
        <button class="tab-btn" onclick="switchTab('${p.id}', 'code', this)">Python Implementation</button>
        <button class="tab-btn" onclick="switchTab('${p.id}', 'run', this)">Execution & Output</button>
        <button class="tab-btn" onclick="switchTab('${p.id}', 'trouble', this)">Troubleshooting & Safety</button>
      </div>

      <!-- Tab 1: Overview -->
      <div class="tab-pane active" id="pane_${p.id}_overview">
        <div class="section-block">
          <div class="section-label">🎯 Aim of Experiment</div>
          <div class="aim-box">${p.aim}</div>
        </div>

        <div class="section-block">
          <div class="section-label">📚 Learning Objectives</div>
          <ul class="bullet-list">
            ${p.objectives.map(obj => `<li>${obj}</li>`).join("")}
          </ul>
        </div>

        <div class="section-block">
          <div class="section-label">🧰 Components Required</div>
          <ul class="bullet-list">
            ${p.components.map(c => `<li>${c}</li>`).join("")}
          </ul>
        </div>
      </div>

      <!-- Tab 2: Wiring -->
      <div class="tab-pane" id="pane_${p.id}_wiring">
        <div class="section-block">
          <div class="section-label">🔌 Hardware Connection Table (BCM Scheme)</div>
          <div class="table-wrapper">
            <table class="custom-table">
              <thead>
                <tr>
                  <th>Component / Module Terminal</th>
                  <th>Raspberry Pi GPIO Pin</th>
                  <th>Circuit Notes & Protection</th>
                </tr>
              </thead>
              <tbody>
                ${p.wiring.map(w => `
                  <tr>
                    <td><strong>${w.component}</strong></td>
                    <td><code style="color: var(--accent-cyan); font-weight: bold;">${w.pin}</code></td>
                    <td>${w.note}</td>
                  </tr>
                `).join("")}
              </tbody>
            </table>
          </div>
        </div>

        ${p.pins.length > 0 ? `
          <div class="callout callout-info">
            <div class="callout-icon">💡</div>
            <div>
              <strong>Active GPIO Pins for this Practical:</strong> 
              ${p.pins.map(pin => `<code>BCM GPIO ${pin}</code>`).join(", ")}. 
              Hover over this practical card to locate these pins on the 40-Pin board diagram above.
            </div>
          </div>
        ` : ''}
      </div>

      <!-- Tab 3: Python Code -->
      <div class="tab-pane" id="pane_${p.id}_code">
        <div class="section-block">
          <div class="code-container">
            <div class="code-header">
              <span>examples/practical_${p.id}/main.py</span>
              <button class="btn-copy" onclick="copyCode('code_${p.id}', this)">📋 Copy Script</button>
            </div>
            <pre class="code-block" id="code_${p.id}"><code>${escapeHtml(p.code)}</code></pre>
          </div>
        </div>
      </div>

      <!-- Tab 4: Run & Output -->
      <div class="tab-pane" id="pane_${p.id}_run">
        <div class="section-block">
          <div class="section-label">🚀 Execution Command</div>
          <div class="code-container">
            <div class="code-header">
              <span>CLI Execution</span>
              <button class="btn-copy" onclick="navigator.clipboard.writeText('${p.cliCommand}'); this.innerText='Copied!'">📋 Copy</button>
            </div>
            <pre class="code-block"><code>${p.cliCommand}
# Alternatively:
python examples/practical_${p.id}/main.py</code></pre>
          </div>
        </div>

        <div class="section-block">
          <div class="section-label">🖥️ Expected Terminal Output</div>
          <div class="code-container">
            <div class="code-header"><span>Console Output</span></div>
            <pre class="code-block" style="color: #38bdf8;"><code>${escapeHtml(p.expectedOutput)}</code></pre>
          </div>
        </div>
      </div>

      <!-- Tab 5: Troubleshooting & Safety -->
      <div class="tab-pane" id="pane_${p.id}_trouble">
        <div class="section-block">
          <div class="section-label">⚠️ Laboratory Safety Warnings</div>
          <div class="callout callout-warning">
            <div class="callout-icon">⚡</div>
            <div>${p.safetyNotes}</div>
          </div>
        </div>

        <div class="section-block">
          <div class="section-label">🛠️ Common Troubleshooting Diagnostics</div>
          <ul class="bullet-list">
            ${p.troubleshooting.map(t => `<li>${t}</li>`).join("")}
          </ul>
        </div>
      </div>
    </article>
  `).join("");
}

// Tab Switching Helper
function switchTab(practicalId, tabName, btnElement) {
  const card = document.getElementById(`practical_${practicalId}`);
  if (!card) return;

  // Deactivate all headers in card
  card.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
  btnElement.classList.add("active");

  // Deactivate all panes in card
  card.querySelectorAll(".tab-pane").forEach(pane => pane.classList.remove("active"));
  const targetPane = document.getElementById(`pane_${practicalId}_${tabName}`);
  if (targetPane) targetPane.classList.add("active");
}

// Event Listeners
function setupEventListeners() {
  // Search
  const searchInput = document.getElementById("searchPracticals");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      currentSearch = e.target.value;
      renderPracticals();
    });
  }

  // Filter Chips
  document.querySelectorAll(".filter-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      document.querySelectorAll(".filter-chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      currentFilter = chip.dataset.filter;
      renderPracticals();
    });
  });
}

function scrollToPractical(id) {
  const el = document.getElementById(`practical_${id}`);
  if (el) {
    el.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

function copyCode(elementId, btn) {
  const text = document.getElementById(elementId).innerText;
  navigator.clipboard.writeText(text).then(() => {
    const original = btn.innerHTML;
    btn.innerHTML = "✅ Copied!";
    setTimeout(() => { btn.innerHTML = original; }, 2000);
  });
}

function escapeHtml(string) {
  return String(string).replace(/[&<>"']/g, function (s) {
    return ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[s];
  });
}
