var request = require('request');


//메타버스(Metaverse)세계와 우리의 미래
exports.main = async function(req, res){
    return res.render("main.ejs");
}

exports.searching = async function(req, res){
    console.log("검색어 입력 >> ", req.query.reportTitle);
    console.log("선택 >> ", req.query.algorithm);
    
    const userInput = req.query.reportTitle;
    const checked = req.query.algorithm;
    return res.render("searching.ejs", {userInput, checked});
}

exports.let = async function(req, res){
    const file_name=  req.body.userInput; //string
    const file_checked = req.body.userChecked;
    const YoloResult = (callback)=>{
        const options = {
            method: 'POST',
            uri: "http://127.0.0.1:5000/test",
            qs: {
                file_name: file_name,
                file_checked: file_checked
        
            }
        }

        request(options, function (err, res, body) {
            callback(undefined, {
                result:body
            });
        });
    }

    YoloResult((err, {result}={})=>{
        if(err){
            console.log("error!!!!");
            res.send({
                message: "fail",
                status: "fail"
            });
        }
        else{
            console.log("flask로부터 받아온 정보 >> ", result);
            res.send(result);
        }
        
    })
    
}

exports.info = async function(req, res){
    return res.render("info.ejs");
}

exports.domestic = async function(req, res){
    return res.render("domestic.ejs");
}

exports.abroad = async function(req, res){
    return res.render("abroad.ejs");
}
