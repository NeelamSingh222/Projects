var express = require('express');
var app=express();

app.get('/',function(req,res){
	res.send("hi there");
});

app.get('/speak/:animals',function(req,res){
	var a=req.params.animals;
	var b={
		pig:"opig",
		cat:"omeow",
		wolf:"onu"
	};
	res.send(" the "+a+" says '"+b[a]+" '");
});

app.get("/:thing/:times",function(req,res){
	var a=req.params.thing;
	var b=req.params.times;
	var s="";
	for (var i=0;i<b;i++){
		s+=a+" ";
	}
	res.send(s);
});

app.get("*",function(req,res){
	res.send(" do hell with your life ");
});

app.listen(3000,"127.0.0.1",function(){
	console.log(" server is running ");
});
