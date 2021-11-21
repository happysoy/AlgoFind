const indexDao = require("../dao/indexDao");
var request = require('request');

exports.main = async function(req, res){
    return res.render("main.ejs");
}

exports.searching = async function(req, res){
    console.log("검색어 입력 >> ", req.query.reportTitle);
    const userInput = req.query.reportTitle;
    return res.render("searching.ejs", {userInput});
}

exports.let = async function(req, res){
    const file_name=  req.body.userInput; //string

    const YoloResult = (callback)=>{
        const options = {
            method: 'POST',
            uri: "http://127.0.0.1:5000/test",
            qs: {
                file_name: file_name
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
            let json = JSON.parse(result);

            const data = { message: "from flask", status: "success", data:{json } };
            res.send(data);
            
        }
        
    })
    
}
