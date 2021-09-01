console.log('chinese-article-formatter by memset0.')

document.getElementById('button').onclick = function () {
	const options_name = [
		'delete-spaces',
		'delete-blank-lines',
		'convert-half-width-punctuation',
	];

	let options = {};
	for (const name of options_name) {
		options[name] = document.getElementById(name).checked;
	}

	document.getElementById('text').value = format(document.getElementById('text').value, options);
};

function format(text, options) {
	if (options['delete-spaces']) {
		text = text.replace(/[^\S\n]/g, '');
	}

	if (options['delete-blank-lines']) {
		text = text.replace(/\n{2,}/g, '\n')
	}

	if (options['convert-half-width-punctuation']) {
		text = text
			.replace(/\!/g, '！')
			.replace(/\?/g, '？')
			.replace(/\./g, '。')
			.replace(/\,/g, '，')
			.replace(/\;/g, '；')
			.replace(/\:/g, '：')
			.replace(/\(/g, '（')
			.replace(/\)/g, '）')
			.replace(/\-{2,}/g, '——')
	}

	return text;
}