console.log('pinyin-tone-marker by memset0.');
console.log('https://github.com/memset0/naive-toys/blob/master/pinyin-tone-marker');

String.prototype.replaceAll = function (search, replacement) {
	var target = this;
	return target.split(search).join(replacement);
};

document.getElementById('button').onclick = function () {
	const options_name = [
		'space-needed',
		'bracket-needed',
		'blank-mode',
	];

	let options = {};
	for (const name of options_name) {
		options[name] = document.getElementById(name).checked;
	}

	document.getElementById('text').value = format(document.getElementById('text').value, options);
};

function format(text, options) {
	const charmap = 'aoeiu';
	const tonemap = 'āáǎàōóǒòēéěèīíǐìūúǔùǖǘǜ';

	for (let i in charmap) {
		for (let j = 1; j <= 4; j++) {
			text = text.replaceAll(charmap[i] + String(j), tonemap[i * 4 + j - 1]);
		}
	}

	text = text.replaceAll('v', 'ü');

	const pinyin_reg = new RegExp('([a-zA-Zü' + tonemap + ']+)', 'g');
	text = text.replace(pinyin_reg, (match) => {
		if (options['blank-mode']) {
			match = '______';
		}

		if (options['bracket-needed']) {
			match = '(' + match + ')';
		}

		if (options['space-needed']) {
			match = ' ' + match + ' ';
		}

		return match;
	});

	return text;
}