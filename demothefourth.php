<?php

require_once('clsDB.cls.php');

$db = new dbCls();

$host = 'localhost';
$username = 'northwind';
$password = 'n0rthwind';
$dbname = 'northwind';
$errStr = '';
$opStr = '';

$db->_dbHost = "localhost";
$db->_dbUsername = "northwind";
$db->_dbPassword = "n0rthwind";
$db->_dbName = "northwind";

$link = $db->dbConnect($host,$username,$password);

if(!$link)
{
	die( $db->dbError() );
}
else
{
	if(!$db->dbSelect($dbname))
	{
		$errStr = '<p>db connect failed!</p>';
	}
	else
	{
		// database and server connected ok - continue with page
		$sql = "select CompanyName from Customers limit 4";
		if(!($result=$db->dbExec($sql)))
		{
			$errStr = '<p>error with query!'.$db->dbError().'</p>';
		}
		else
		{
			// query ran ok - process any results
			$opStr .= '<ul>';
			while($r=$db->dbFetchRow($result))
			{
				$opStr .= '<li>'.$r[0].'</li>';
			}
			$opStr .= '</ul>';
		}
	}
}

?>
<html>
	<head>
		<title>DB Class EG.#2</title>
		<link href="./dbClsMain.css" rel="stylesheet" type="text/css" />
		<link type="text/css" href="../bluesy/css/custom-theme/jquery-ui-1.8.7.custom.css" rel="stylesheet" />	
		<script type="text/javascript" src="../bluesy/js/jquery-1.4.4.min.js"></script>
		<script type="text/javascript" src="../bluesy/js/jquery-ui-1.8.7.custom.min.js"></script>

		<script type="text/javascript">
		  $(document).ready(function() {
		  
			//.ajaxSetup ({ cache: false; });
			var xhr;
			
			//slider example 1: a default slider
			$("#slider1").slider({
				range: false,
				min: 1,
				max: 360,
				slide: function(event, ui) {
					$("#value1").val(ui.value);
					var p = ui.value;
					$("#imgpos").css({
					  left: (14 +p*1.18) + "px",
					  top: (145 -(Math.sin(p/50.929)*110)) + "px"
					}).show();
					// ajax request here?
					if(xhr) xhr.abort();
					xhr = $.ajax({					  
						url: 'retrievegraphdata.php',
						data: "",
						//dataType: 'json',
						success: function(data) {
						  var str = data;
						  $('#results').html(str);
						}
					});
				}
			});
		  });
		</script>
		<style>
			form {
				width:  50%;
			}
			form input {
				margin-bottom:12px;
				width:6em;
			}
			#slider1 {
				margin-left:10px;
				width: 75%;
			}
			.dynImageLoc {
			  width: 400px;
			  border: dotted 1px silver;
			  position: relative;
			  top: 0px;
			  left: 0px;
			}
			#graph {
				position: relative;
				top: 0px;
				left: 0px;
				border: solid 2px blue;
			}
			#imgpos {
			  position:absolute;
			  top: 145px;
			  left: 15px; 
			  width: 16px;
			  height: 16px;
			}
			#results {
			  padding: 3px;
			  border: solid 1px #3366cc;
			  width: 480px;
			  position: absolute;
			  top: 100px;
			  right: 50px;
			  box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.75);
			  -moz-box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.75);
			  -webkit-box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.75);
			}
		</style>
		<style type="text/css">
			.ui-slider-horizontal .ui-state-default {background: white url(./images/edit-delete.png) no-repeat scroll 50% 50%;border:none;}
		</style>

	</head>
	<body>
		<div class="headerSection">
			<h1>Details Page</h1>
		</div>
		
		<div class="contentSection">

			<!-- display any error messages -->
			<?php if($errStr) echo $errStr;?>
			
			<!-- display any current data string -->
			<h2>Current items</h2>
			<div class="currentDataSection">
				<?php if($opStr) echo $opStr;?>
			</div>
			
			<div class="dynImageLoc">
			  <!--<img id="graph" src="./images/graph_460x300.png" />-->
			  <img id="graph" src="./createdyngraph.php" />
			  
			  <!-- range for imgpos is from 14 to 440 (426px) -->
			  <img id="imgpos" src="./images/ball_16x16.png" />
			</div>
			<form action="" method="get">
				X pos:<input type="text" id="value1" />
				<div id="slider1"></div>
			</form>
			
			<div id="results">
			some text
			</div>
			<!--/ display a link to previous page -->
			<p><a href="#" onclick="location.href=document.referrer">back</a></p>
			
		</div> <!-- end content section-->
	<body>
	</body>
</html>