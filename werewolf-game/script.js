const werewolf = {
	$button: [],

	onButtonClick(index) {
		console.log('click', index);
	},

	onWindowResize() {
		const width = window.innerWidth || document.body && document.body.clientWidth;
		const height = window.innerHeight || document.body && document.body.clientHeight;

		const panelHeight = Math.floor(Math.min(height * 0.6, width / 3 * 4));
		const buttonWidth = Math.floor(width / 3) - 6;
		const buttonHeight = Math.floor(panelHeight / 4) - 12;
		const logoSize = Math.min(width, height) / 2 - 2;

		// panel
		document.getElementById('panel').style.height = panelHeight + 'px';
		document.querySelectorAll('#panel .row').forEach(e => e.style.height = e.style['line-height'] = buttonHeight + 'px');
		document.querySelectorAll('#panel .row .col').forEach(e => e.style.width = (buttonWidth - 32) + 'px');

		// index
		document.getElementById('logo').style.height = logoSize + 'px';
		document.getElementById('logo').style.padding = logoSize / 2 + 'px';
		document.getElementById('index').style.height = (logoSize * 2 + 32) + 'px';
		document.getElementById('index').style['margin-top'] = (height - logoSize * 2 - 32) / 2 + 'px';

		console.log('window', { width, height, panelHeight });
	},

	gotoSence(sence) {
		const hideElement = ($element) => $element.style.display = 'none';
		const showElement = ($element) => $element.style.display = 'block';
		switch (sence) {
			case 'start':
				hideElement(document.getElementById('panel'));
				break;
		}
	},

	initialize() {
		for (let i = 1; i <= 12; i++) {
			werewolf.$button[i] = document.getElementById('btn-' + (i < 10 ? '0' : '') + i);
			werewolf.$button[i].onclick = function () {
				werewolf.onButtonClick(i);
			}
		}
		window.onresize = werewolf.onWindowResize;
		werewolf.onWindowResize();
		werewolf.gotoSence('start');
	}
};


werewolf.initialize();