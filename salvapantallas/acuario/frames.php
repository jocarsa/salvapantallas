<html>
    <head>
        <style>
            body,html{padding:0px;margin:0px;overflow:hidden;background:black;}
            iframe{border:0px;position:absolute;top:0px;left:0px;}
            #frame1{filter:blur(3px);}
            #frame2{filter:blur(2px);}
            #frame3{filter:blur(1px);}
        </style>
        
    </head>
    <body>
        <iframe src="index.html" width=1920 height=1080 id="frame1"></iframe>
        <iframe src="index.html" width=1920 height=1080 id="frame2"></iframe>
        <iframe src="index.html" width=1920 height=1080 id="frame3"></iframe>
        <iframe src="index.html" width=1920 height=1080 id="frame4"></iframe>
        
        <script>
            var anchura = window.innerWidth;
            var altura = window.innerHeight;
            document.getElementById("frame1").width=anchura;
            document.getElementById("frame1").height=altura;
            
            document.getElementById("frame2").width=anchura;
            document.getElementById("frame2").height=altura;
            
            document.getElementById("frame3").width=anchura;
            document.getElementById("frame3").height=altura;
            
            document.getElementById("frame4").width=anchura;
            document.getElementById("frame4").height=altura;
            
        </script>
    </body>
</html>