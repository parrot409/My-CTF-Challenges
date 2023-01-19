I was expecting around 5 solves for this challenge but it turned out to be easier than i expected. It was because it was solvable without the "little-known trick" i had in mind. Nevertheless, I think it was a good challenge for more experienced beginners since the trick to solve this is documented by a website with a great SEO ranking (portswigger blog).

```htmlmixed
<!-- 
csp: default-src 'self'; script-src 'unsafe-eval' 'nonce-$nonce$'
-->
<html>
	<head>
		<title>hi</title>
	</head>
	<body>
		<h1>definitely not vulnerable to XSS</h1>
		<div>
			$html_injection$
		</div>
		<script nonce="$nonce$">
			try{
				eval(window.h.a.p.p.y._.n.e.w._.y.e.a.r._.h.a.c.k.e.r.s.toString())
			}catch(e){}
		</script>
    </body>
</html>
```

There is a html injection vulnerablity in this page and the player should steal the cookies. Injecting script or event-based payloads don't work because of the csp.

DOM Clobbering has become well-known in the past years so it shouldn't be hard to figure out that the `window.h.a.p.p.y...` property should be clobbered ( if you have experience about client-side stuff of course ).

To clobber that many property levels, the player needs to find out about the [*nested iframe* technique](https://portswigger.net/research/dom-clobbering-strikes-back). [This blogpost by portswigger](https://portswigger.net/research/dom-clobbering-strikes-back) mentions that normally, when you inject your html payload, the script can't access the properties that are inside the iframe because they are not rendered by chrome. The blogpost also mentions a way to solve this issue which is using "style imports" in a style tag. I wanted to disallow players to use this "style imports" technique so i blocked the usage of inline-css with csp. The intended way to solve this is using the "blocking" attribute of link tags. 

```htmlmixed!
<iframe srcdoc="oh"></iframe>
</iframe>
<link blocking="render" href="critical-font.woff2" as="font"/>
<script>/*script*/</script>
```

The above link tag stops the html-rendering while fetching the font so it gives the iframe an enough time to render. But it was also possible to solve this by injecting many stylesheet link tags which i thought it's not possible.

