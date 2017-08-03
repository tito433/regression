import re

string="""
aLayer.push({
'event': 'rollupFirePageview',
'rollupPageViewUrl': url
});
}
function updateAd(){
googletag.cmd.push(function () {
googletag.pubads().refresh();
});
}
function updateAdgalleryTracking(slideNumber){ updateAd();galleryTracking(slideNumber);}
if (window.addEventListener)
window.addEventListener('resize', updateAd,false);
else if (window.attachEvent)
window.attachEvent("onresize", updateAd);
</script>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TKCPH93');</script>
<meta name="google-site-verification" content="F7Hv0gB_VqEp-aygJ41g4YKy9uDLME2gwa7Kc72He2E" />
<!--[if lt IE 9]>
<script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js" defer></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/respond.js/1.4.2/respond.min.js" defer></script>
<![endif]-->
<script>(function(w,d,u){w.readyQ=[];w.bindReadyQ=[];function p(x,y){if(x=="ready"){w.bindReadyQ.push(y);}else{w.readyQ.push(x);}};var a={ready:p,bind:p};w.$=w.jQuery=function(f){if(f===d||f===u){return a}else{p(f)}}})(window,document)</script>
</head>
<body class="article_433_10433">
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TKCPH93"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- Powered by Escenic Content Engine and Widget Framework. http://escenic.com -->
<div class=" ">
<style>
.addthis_share{
text-align:center;
}
.addthis_share_button{
width:44px;
height:44px;
cursor:pointer;
display:inline-block;
}
.addthis_share_button.facebook{
background: url("http://www.globalblue.com/static/theme/global-blue-2017/base/images/icon/social/social_fb@2x.png") center center no-repeat;
background-size:44px;
}
.addthis_share_button.twitter{
background: url("http://www.globalblue.com/static/theme/global-blue-2017/base/images/icon/social/social_tw@2x.png") center center no-repeat;
background-si

"""
m=re.search('article_(\d+)_(\d+)',string)
if m:
	print m.group()
	print m.group(1)
	print m.group(2)