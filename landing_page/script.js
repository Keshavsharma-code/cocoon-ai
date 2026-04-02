document.addEventListener('DOMContentLoaded', () => {
    // 1. Terminal Simulation
    const termBody = document.getElementById('term-body');
    const commands = [
        { text: '$ cocoon run --pupa', type: 'cmd' },
        { text: '🦋 Entering Pupa Phase...', type: 'info' },
        { text: '✓ Silk layer initialized.', type: 'success' },
        { text: 'LARVA-DESIGNER', type: 'thinking', label: 'is crafting aesthetics...' },
        { text: '✨ Metamorphosis complete!', type: 'success' }
    ];

    let cmdIndex = 0;
    function addTerminalLine() {
        if (cmdIndex >= commands.length) return;
        
        const cmd = commands[cmdIndex];
        const line = document.createElement('div');
        line.className = 'line';
        
        if (cmd.type === 'cmd') {
            line.innerHTML = `<span>$</span> ${cmd.text.slice(2)}`;
        } else if (cmd.type === 'info') {
            line.className += ' status-info';
            line.innerText = cmd.text;
        } else if (cmd.type === 'success') {
            line.className += ' status-success';
            line.innerText = cmd.text;
        } else if (cmd.type === 'thinking') {
            line.className += ' thinking';
            line.innerHTML = `<span>${cmd.text}</span> <span class="typing">${cmd.label}</span><span class="dots"></span>`;
        }

        termBody.appendChild(line);
        termBody.scrollTop = termBody.scrollHeight;
        cmdIndex++;
        setTimeout(addTerminalLine, 1500 + Math.random() * 1000);
    }

    setTimeout(addTerminalLine, 4000);

    // 2. Scroll Animations (Reveal on Scroll)
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.arch-card, .larva-card, .section-title, .install-section').forEach(el => {
        el.classList.add('reveal');
        observer.observe(el);
    });

    // 3. Copy Button Logic
    const copyBtn = document.querySelector('.copy-btn');
    const copyText = document.querySelector('.copy-box code');

    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(copyText.innerText).then(() => {
            copyBtn.innerText = 'Copied!';
            copyBtn.style.background = '#27C93F';
            setTimeout(() => {
                copyBtn.innerText = 'Copy';
                copyBtn.style.background = '#FFFFFF';
            }, 2000);
        });
    });

    // 4. Parallax Background Shadow
    document.addEventListener('mousemove', (e) => {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        
        const heroImage = document.querySelector('.hero-image');
        if (heroImage) {
            heroImage.style.transform = `scale(1.05) translate(${(x - 0.5) * 20}px, ${(y - 0.5) * 20}px)`;
        }
    });

    // 5. Swarm Flow Interaction
    const nodes = {
        'mother-node': { title: '1. Intent Analysis', desc: 'Mother parses natural language goals into atomic, sequential subtasks with dependency mapping.' },
        'hive-node': { title: '2. Hive Orchestration', desc: 'The Rust-powered Hive manages high-performance communication and state synchronization between agents.' },
        'larva-coder': { title: '3a. Larva-Coder', desc: 'Specialized in writing production-ready code (Rust/Python) and solving complex architectural problems.' },
        'larva-designer': { title: '3b. Larva-Designer', desc: 'Crafts premium UI/UX components and ensures visual excellence across the entire stack.' },
        'larva-tester': { title: '3c. Larva-Tester', desc: 'Self-verifying agent that runs automated test-driven metamorphosis to ensure zero-bug delivery.' }
    };

    document.querySelectorAll('.node').forEach(node => {
        node.addEventListener('click', () => {
            const type = [...node.classList].find(c => nodes[c] || nodes[node.id]);
            const data = nodes[type] || nodes[node.id];
            if (data) {
                const detailBox = document.querySelector('.detail-box');
                detailBox.innerHTML = `<h4>${data.title}</h4><p>${data.desc}</p>`;
                
                document.querySelectorAll('.node').forEach(n => n.classList.remove('highlight'));
                node.classList.add('highlight');
            }
        });
    });
});

// 6. Legal Modals
const legalContent = {
    terms: `<h2>Terms of Service</h2>
            <p><strong>1. ABSOLUTELY NO WARRANTY:</strong> This software is provided "AS IS" without warranty of any kind. The author (Keshav Sharma) is NOT responsible for any damages, data loss, or financial loss incurred while using this tool.</p>
            <p><strong>2. LIMITATION OF LIABILITY:</strong> In no event shall the author be liable for any claims, damages, or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software.</p>
            <p><strong>3. USER RESPONSIBILITY:</strong> You are 100% responsible for the actions taken by the agent swarm, including but not limited to file modifications, terminal commands, and API costs.</p>
            <p><strong>4. NO LEGAL RECOURSE:</strong> By using this software, you waive any and all rights to pursue legal action against the author.</p>`,
    privacy: `<h2>Privacy Policy</h2>
              <p><strong>1. LOCAL FIRST:</strong> Cocoon is a local-first application. No data is collected, stored, or transmitted to any third-party servers managed by the author.</p>
              <p><strong>2. API KEYS:</strong> Your API keys (Gemini, OpenAI, etc.) are stored locally in your environment variables. Never share these keys.</p>
              <p><strong>3. TELEMETRY:</strong> There is zero telemetry or usage tracking built into the core engine.</p>`
};

function toggleModal(type) {
    const modal = document.getElementById('legal-modal');
    const text = document.getElementById('legal-text');
    if (type) {
        text.innerHTML = legalContent[type];
        modal.style.display = 'block';
    } else {
        modal.style.display = 'none';
    }
}

window.onclick = function(event) {
    const modal = document.getElementById('legal-modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
