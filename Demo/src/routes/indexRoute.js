const index = require("../controllers/indexController");

module.exports = function(app) {
    app.get('/', index.main); //메인화면

    app.get('/searching', index.searching); //사용자가 논문 제목 입력
    app.post('/let', index.let); //input title backtracking으로 searching

}