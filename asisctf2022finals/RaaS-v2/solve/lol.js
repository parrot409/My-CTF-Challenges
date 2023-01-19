var dns = require('native-dns');
var server = dns.createServer();

server.on('request', function (request, response) {
  console.log(request.question)
  response.answer.push(dns.CNAME({
    name: request.question[0].name,
    data: '172.32.12.2.lmao.pwnn.net/internal/',
    ttl: 600,
  }));
  response.send();
});

server.on('error', function (err, buff, req, res) {
  console.log(err.stack);
});

server.serve(53,'172.32.12.1');
