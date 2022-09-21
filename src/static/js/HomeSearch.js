const searchForm = document.getElementById('SearchInput')
const resultBox = document.getElementById('result-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
console.log(csrf)

const sendSearchedData = (film) => {
	$.ajax({
		type: 'POST',
		url: 'search/',
		data: {
			'csrfmiddlewaretoken': csrf,
			'film': film
		},
		success: (res)=>{
			console.log(res.data)
			const data = res.data
			if (Array.isArray(data)) {
				resultBox.innerHTML = ""
				data.forEach(film=> {
					resultBox.innerHTML += `
						<a href="film/${film.pk}" class="item">
							<div class="row mt-2 mb-2">
								<div class="col-2">
									<div class="film-pic">
										<img src="https://kinopoiskapiunofficial.tech/images/posters/kp/${film.pk}.jpg" alt="">
									</div>
								</div>
								<div class="col-10">
									<h5>${film.name}</h5>
								</div>
							</div>
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