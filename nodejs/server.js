var http = require('http');
var url = require('url');
var fs = require('fs');
var mysql = require('mysql');
var nodeStatic = require('node-static');

var conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb"
});

conn.connect(function(err) {
  if (err) throw err;
  console.log("Connected to database!");
});

http.createServer(function (req, res) {
  var q = url.parse(req.url, true);
  var filename = "./pages" + q.pathname + ".html";
  var fileServer = new nodeStatic.Server('./public');

  // fileServer.serve(req, res);

  if (q.pathname == "/") {
    filename = "./pages/index.html";
  }
  
  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found");
    } 
    res.writeHead(200, {'Content-Type': 'text/html'});
    // res.writeHead(200, {'Content-Type': 'text/css'});
    res.write(data);
    return res.end();
  });

  function serveFile(req, res) {
    fileServer.serve(req, res, function (err, result) {
      if (err) {
        console.error("Error serving " + req.url + " - " + err.message);
        res.writeHead(err.status, err.headers);
        res.end();
      }
    });
  }

}).listen(1337, console.log("Server running at http://localhost:1337"));
