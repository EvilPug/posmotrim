const searchForm = document.getElementById('SearchInput')
const resultBox = document.getElementById('result-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const sendSearchedData = (username) => {
	$.ajax({
		type: 'POST',
		url: 'search/',
		data: {
			'csrfmiddlewaretoken': csrf,
			'username': username
		},
		success: (res)=>{
			console.log(res.data)
			const data = res.data
			if (Array.isArray(data)) {
				resultBox.innerHTML = ""
				data.forEach(srch_user=> {
					resultBox.innerHTML += `
						<a href="/users/${srch_user.pk}" class="item">
							${srch_user.name}
						</a>
						<hr>
					`
				})
			} else {
				if (searchForm.value.length > 0) {
					resultBox.innerHTML = `<b>${data}</b>`
				} else {
					resultBox.classList.add('not-visible')
				}
			}
		},
		error: (err) => {
			 console.log(err)
		}

	})
}

searchForm.addEventListener('keyup', e=> {
	if (resultBox.classList.contains('not-visible')) {
		resultBox.classList.remove('not-visible')
	}

	sendSearchedData(e.target.value)
})