<html>
    <head>
        <style>
            html,body{text-align:center;width:100%;height:100%;padding:0px;margin:0px;overflow:hidden;}
            iframe{border:0px;overflow:hidden;}
            .container {
                  height: 100%;
                  position: relative;
                  border: 0px solid green;
                }

                .center {
                  margin: 0;
                  position: absolute;
                  top: 50%;
                  left: 50%;
                  -ms-transform: translate(-50%, -50%);
                  transform: translate(-50%, -50%);
                }
        </style>
    </head>
    <body class="container">
       <!-- <div class="center" style="width:910px;height:300px;">-->
        <?php
        for($i = 0;$i<28;$i++){ 
        ?>
        <iframe width=300 height=300 src="ui.html" scrolling="no"></iframe>
        <?php
        } 
            ?>
           <!-- </div> -->
    </body>
</html>