(function() {
    if (window.myBooklet !== undefined) {

    } else {
        document.body.appendChild(document.createElement('script')).src = 'http://127.0.0.1:8000/static/js/bookmark.js?r=' + Math.floor(Math.random().*99999999999999999);

    }
})();