
NOT_LOGGED_IN_BESTIARY_PAGE_1 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flight Rising </title>

<link rel="stylesheet" type="text/css" href="/includes/custom-theme/jquery-ui-1.8.19.custom.css" />
<link rel="stylesheet" type="text/css"  href="/includes/2_1.css" />

<script type="text/javascript" src="/js/jquery-1.9.1.js"></script>
<script type="text/javascript" src="/js/jquery.hoverIntent.js"></script>
<script type="text/javascript" src="/js/jquery-ui-1.9.2.js"></script>
<script type="text/javascript" src="/js/jquery.cluetip.min.js"></script>
<script type="text/javascript" src="/js/ed.js"></script>

<script type="text/javascript">
function helpMe(tut, first){
	$('body').append('<div id="tutorial"></div>');
	$("#tutorial").html('<img src="/images/layout/loading.gif"> loading...');

	$.ajax({
		type: "POST",
		data: {tut: tut, ret: "title"},
		url: "/includes/ol/tutorial.php",
		cache:false
	}).done(function(stuff){
		var tuttitle = stuff;

		//if(tut == "hoard"){var wval = 400;}
		//else{wval = 400;}

		var wval = 400;

		$('#tutorial').dialog({
			autoOpen: false,
			title: tuttitle,
			width: wval,
			height: "auto",
			modal: true,
			resizable: false,
			draggable: false,
			closeOnEscape: false,
			position: ['center', 100],
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
			}
		});

		$('#tutorial').dialog('open');

		$.ajax({
			type: "POST",
			data: {tut: tut, ret: "modal", first: first},
			url: "/includes/ol/tutorial.php",
			cache:false
		}).done(function(bodystuff){
			$("#tutorial").html(bodystuff);
		});


	});


}

function pregiveStar(id)
{

	$.each(id, function(index, value){

		var time = index * 7000;
		//alert(time +":"+ value);
		setTimeout( function(){giveStar(value)}, time);
		//setTimeout(function(){giveStar('5')}, 3000);
	});
}

function giveStar(id)
{

	$("#achieve_pop").html('<img src="/../../images/layout/loading.gif"> loading...');

	$('#achieve_pop').dialog({
		autoOpen: false,
		title: "Achievement Unlocked!",
		width: 310,
		height: 120,
		position: {
			my: 'left',
			at: 'right',
			of: $('#logo')
		},
		modal: false,
		resizable: false,
		draggable: false,
		closeOnEscape: false,
		open: function(event, ui) {
			$(".ui-dialog-titlebar-close", ui.dialog).hide();
		}
	});

	$.ajax({
		data: {id: id},
		url: "/includes/ol/achieve_pop.php",
		cache:false
	}).done(function(stuff){
		$('#achieve_pop').dialog('open');

		$("#achieve_pop").html(stuff);

		$('#achieve_pop').parent().fadeIn(1000);

		$("#achieve_pop").parent().delay(5000).fadeOut(1000);



		$('#overlay_ach').fadeIn(1).animate({height:'50px', width:'50px'}, 1).animate({height:'25px', width:'25px'}, 1000).fadeOut(1000);
	});


}

var starmie = Array();
</script>

<script type="text/javascript">
//<![CDATA[
//CLUETIP
$(document).ready(function() {
	$('a.clue').cluetip({
		height:"auto",
		ajaxCache: true
	});

	$('a.clueitem').cluetip({
		height:130,
		showTitle:false,
		positionBy: 'mouse',   // Sets the type of positioning: 'auto', 'mouse','bottomTop', 'topBottom', fixed'
		topOffset: 20,       // Number of px to offset clueTip from top of invoking element
		leftOffset: -20,       // Number of px to offset clueTip from left of invoking element
		ajaxCache: true
	});

	$('a.cluestat').cluetip({
		width: 180,
		height: "auto",
		ajaxCache: true
	});

	$('a.clue_nrg').cluetip({
		showTitle:false,
		width:300,
		height: "auto"
	});

	$('a.loginbar').cluetip({
		splitTitle: '|',
		showTitle:false,
		width: 200,
		height: 'auto',
		leftOffset: 25
	});

	$('a.miniclue').cluetip({
		splitTitle: '|',
		showTitle:false,
		width:100,
		height: 'auto',
		leftOffset: 25
	});

	$('a.miniclue_female').cluetip({
		splitTitle: '|',
		showTitle:false,
		width:100,
		height: 'auto',
		leftOffset: 25
	});

	$('a.miniclue_male').cluetip({
		splitTitle: '|',
		showTitle:false,
		width:50,
		height: 'auto',
		leftOffset: 25
	});

	$('a.elemclue_fire').cluetip({
		splitTitle: '|',
		showTitle:false,
		width:80,
		height: 'auto',
		leftOffset: 25
	});

	$('a.cluehelp').cluetip({
		splitTitle: '|',
		showTitle:false,
		width:'auto',
		height: 'auto',
		positionBy: 'mouse',
		leftOffset: '20px'
	});



	$('a.faire_clue').cluetip({
		positionBy: 'mouse',
		topOffset:'30px',
		leftOffset:'40px',
		height:'auto',
		ajaxCache: true
		//tracking: true
	});
});
//]]>
</script>

<script type = "text/javascript">
	function switchTo(qval)
	{
		if (qval)
		{
			document.getElementById('passwordtext').style.display="none";
			document.getElementById('pword').style.display="inline";
			document.getElementById('pword').focus();
		}
		else
		{
			document.getElementById('pword').style.display="none";
			document.getElementById('passwordtext').style.display="inline";
		}
	}


	///Possibly Deprecated if I do an Ajax quote
	function getText(id,user,date)
	{
		var textarea = document.getElementById("message");
		var quote = document.getElementById(id).innerHTML;
		alert(quote);
		// Code for IE
		if (document.selection)
		{
			textarea.focus();
			var sel = document.selection.createRange();
			sel.text = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=0#"+id+"']"+quote+"[/quote]";
		}

		else
    	{  // Code for Mozilla Firefox
			var len = textarea.value.length;
	    	var start = textarea.selectionStart;
			var end = textarea.selectionEnd;


			var scrollTop = textarea.scrollTop;
			var scrollLeft = textarea.scrollLeft;


        	var sel = textarea.value.substring(start, end);
			var rep = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=0#"+id+"']"+quote+"[/quote]";
        	textarea.value =  textarea.value.substring(0,start) + rep + textarea.value.substring(end,len);

			textarea.scrollTop = scrollTop;
			textarea.scrollLeft = scrollLeft;
		}
	}
</script>



</head>




	<body style="background-image: url(/images/layout/none/bg.jpg);">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/none/banner.jpg); position:relative;">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">

<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">
	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	23:21    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">1205 Users Online</a></strong>
	</span>

</div>



</div>


<div id="usertab" style="position:absolute; background-image:url(/images/layout/user_module_bg.png); right:0px; bottom:31px; height:90px; width:285px;">
	<div class="loginform" style="position:relative; width:250px; margin-left:auto; margin-right:auto;">
		<form  method="post" id="loginform">
		<span style="position:absolute; left:0px; top:5px;">
		<input type="text" class="input_reg" name="uname" id="uname" value="Username"  onfocus="if(this.value==this.defaultValue) this.value='';" onblur="this.value=this.value.replace(/^\s+|\s+$/g, ''); if(this.value=='') this.value='Username';" style="width:120px;" />
		</span>

		<span style="position:absolute; left:0px; bottom:5px;">
		<input class="input_reg" type="text" style="width:120px;" id="passwordtext" value="Password" onfocus="switchTo(1)" onkeydown="switchTo(1)">
		<input class="input_reg" type="password" name="pword" id="pword" value="" style="display:none; width:12em;"; onblur="if (this.value=='') {switchTo(0)}">
		</span>

		<span style="position:absolute; left:130px; top:5px; width:100px; display:inline-block; ">
		<input name="remember" type="checkbox" id="remember" value="yes" title="Enabling this option will keep you logged into Flight Rising on this computer." /> <span style="color:#000">Remember Me</span>
		</span>

		<span style="position:absolute; left:130px; bottom:2px;;">
		<input name="button" id="loginbutton" type="submit" value="Login" style="font-size:1em;" />
		</span>
		<input type="hidden" name="dologin" value="Login" id="dologin" />
		</form>
	</div>

	<span style="position:absolute; left:15px; bottom:10px; width:200px; text-align:left; display:inline-block;">
		<a href="index.php?p=reg" class="loginlinks" style="color:#731d08;">Sign Up!</a> | <a href="index.php?p=lostpass" class="loginlinks" style="color:#731d08;">Lost Pass</a>
	</span>

	<script type="text/javascript">
	$('#loginform').submit(function(e) {
		e.preventDefault();
		$('body').append('<div id="logging"></div>');
		$("#logging").html('<img src="/images/layout/loading.gif"> loading...');

		$('#logging').dialog({
			autoOpen: false,
			title: "Login",
			width: 350,
			height: "auto",
			modal: true,
			resizable: false,
			draggable: false,
			closeOnEscape: false,
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
			}
		});

		$('#logging').dialog('open');

		data = $('#loginform').serialize();

		$.ajax({
			type: "POST",
			data: data,
			url: "includes/ol/login.php",
			cache:false
		}).done(function(stuff){
			$("#logging").html(stuff);
		});
	});
	</script>
	</div>

<div id="achieve_pop" style="display:none; overflow:hidden;"></div>

<!--End Banner-->
</div>

<div class="contentcontainer">

<div class="leftcolumn">

<img src="/images/layout/under_shadow.png" width="200px" height="3px" style="position:absolute; z-index:10;"/>

	<div style="position:relative; width:180px; margin:10px;">

		<script type="text/javascript">
	function navDrill(divid) {
		var div = document.getElementById(divid);
		if (div.style.display == "inline") {
			div.style.display = "none";
			document.getElementById(divid + "+").innerHTML = "+";
		} else {
			div.style.display = "inline";
			document.getElementById(divid + "+").innerHTML = "-";
		};
	};
</script>
<style type="text/css">
	.navdrill {
		display: none;
		margin-left: 25px;
	}
	.navbar_drill {
		font-size:10px;
		display:block;
		margin-left:30px;
		color:#731d08;
	}
	.navbar_inline {
		font-size:12px;
		display:inline;
		color:#731d08;
		font-weight: bold;
	}
</style>
	<script type="text/javascript">
	if (document.images)
	{
		var clan_hover = new Image();
		clan_hover.src='/images/layout/header_clan_hover.png';
		var shop_hover = new Image();
		shop_hover.src='/images/layout/header_shop_hover.png';
		var play_hover = new Image();
		play_hover.src='/images/layout/header_play_hover.png';
		var library_hover = new Image();
		library_hover.src='/images/layout/header_library_hover.png';
	}
	</script>

	<a href="main.php?p=unreg"><img src="/images/layout/header_clan.png" border="0" width="179" height="29" onMouseOver="this.src=clan_hover.src" onMouseOut="this.src='/images/layout/header_clan.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Dragon Lair</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Nesting Grounds</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Gather Items</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Clan Profile</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Hoard</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Messages</span></a>

	<a href="main.php?p=unreg"><img src="/images/layout/header_shop.png" border="0" width="179" height="29" onMouseOver="this.src=shop_hover.src" onMouseOut="this.src='/images/layout/header_shop.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=market"><span class="navbar-glow-hover">Marketplace</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Auction House</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Trading Post</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Crossroads</span></a>
	<a class="navbar" href="main.php?p=skins"><span class="navbar-glow-hover">Custom Skins</span></a>

	<a href="main.php?p=unreg"><img src="/images/layout/header_play.png" border="0" width="179" height="29" onMouseOver="this.src=play_hover.src" onMouseOut="this.src='/images/layout/header_play.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Fairgrounds</span></a>
	<a class="navbar" href="main.php?p=unreg"><span class="navbar-glow-hover">Coliseum</span></a>
	<a class="navbar" href="main.php?p=dominance"><span class="navbar-glow-hover">Dominance</span></a>
	<!--<a class="navbar" href="main.php?p=unreg">Adventure</a>-->

	<a href="main.php?p=libraryhome"><img src="/images/layout/header_library.png" border="0" width="179" height="29" onMouseOver="this.src=library_hover.src" onMouseOut="this.src='/images/layout/header_library.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=mb"><span class="navbar-glow-hover">Forums</span></a>
	<a class="navbar" href="main.php?p=explore"><span class="navbar-glow-hover">World Map</span></a>
	<a class="navbar" href="main.php?p=search"><span class="navbar-glow-hover">Search</span></a>
    <a class="navbar" href="main.php?p=scrying"><span class="navbar-glow-hover">Scrying Workshop</span></a>
	<a class="navbar" href="main.php?p=wiki"><span class="navbar-glow-hover">Encyclopedia</span></a>
	<a class="navbar" href="main.php?p=wallpaper"><span class="navbar-glow-hover">Media</span></a>

		<div class="skybanner" style="margin-bottom:10px; margin-top:15px; overflow:hidden;">

		<!-- Skyscraper -->
		<!--/* Zone www.flightrising.com Flight Rising - 160x600 Archive */-->
		<!--/* OpenX iFrame Tag v2.8.11 */-->

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456039264' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456039264' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456039264&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
		<script type='text/javascript' src='http://162.218.115.228/delivery/ag.php'></script>

				</div>
		<!--<div class="skybanner"></div>-->
		<div style="width:80px; height:10px;"></div>
		<!--End Left Column-->
	</div>

</div>

<div class="main">
<!--START CODEMEGEDDON-->

<img src="/images/layout/under_shadow.png" width="750px" height="3px" style="position:absolute; z-index:10;"/>
<img src="/images/layout/bestiary/internal_bg.jpg" style="position:absolute; right:0px;" id="internal_bg" />
<div style="position:relative; width:730px; margin:10px;" id="super-container">
 <a title="Click here to learn more about this page." class="cluehelp"><img src="/images/layout/icon_help.png" style="position:absolute; right:0px; top:0px; z-index:10px; cursor:pointer;" onclick="helpMe('bestiary')" /></a>


<div style="font-size:12px; color:#000;">
		<a href="main.php?p=lair&tab=userpage&id=" style="color:#000;">Clan Profile</a> &raquo;
	<a href="main.php?p=bestiary" style="color:#731d08; font-weight:bold;">Bestiary</a>
</div>


<div style="position:relative; text-align:right; width:705px; height:69px; margin-left:15px; margin-bottom:20px;">
	<span style="font-size:22px; color:#731d08; font-weight:bold; position:absolute; top:20px; left:0px;">Bestiary</span>

	<div style="color:#666; font-size:12px; position:absolute; bottom:10px; left:0px;">
		Chronicles of the beasts you have encountered and collected!
	</div>

	<span style="position:absolute; bottom:25px; right:0px;">
		<span style="margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#731d08; font-weight:bold;" href="main.php?p=bestiary&tab=familiars">Familiars (0)</a>
		</span>
		<!--|
		<span style="margin-left:25px; margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#777777;" href="main.php?p=bestiary&tab=enemies">Enemies (0)</a>
		</span>	-->
	</span>
</div>



<div style="width:700px; margin-left:auto; margin-right:auto;">
	<div style="width:700px; margin-left:auto; margin-right:auto; text-align:center;">
	<div style="width:670px; margin-left:auto; margin-right:auto; text-align:center; margin-bottom:15px; font-size:12px;"><img border="0" src="/images/layout/arrow_left_off.png" style="vertical-align:middle; position:absolute; left:25px;" /> <span style="font-weight:bold;">1</span> <a href='main.php?p=bestiary&tab=familiars&page=2'>2</a> <a href='main.php?p=bestiary&tab=familiars&page=3'>3</a> <a href='main.php?p=bestiary&tab=familiars&page=4'>4</a> <a href='main.php?p=bestiary&tab=familiars&page=5'>5</a> <a href='main.php?p=bestiary&tab=familiars&page=6'>6</a> <a href='main.php?p=bestiary&tab=familiars&page=7'>7</a> <a href='main.php?p=bestiary&tab=familiars&page=8'>8</a> <a href='main.php?p=bestiary&tab=familiars&page=9'>9</a> ... <a href='main.php?p=bestiary&tab=familiars&page=51'>51</a> <a href='main.php?p=bestiary&tab=familiars&page=52'>52</a> <a href="main.php?p=bestiary&tab=familiars&page=2"><img border="0" src="/images/layout/arrow_right.png" style="cursor:pointer; vertical-align:middle; position:absolute; right:25px;" /></a> </div>
			<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/4350_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Abyss Striker</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These observers cluster around ancient aquatic ruins. They may change color to blend with their surroundings.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/16261_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Acid-Tongue Serpenta</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">It is recommended to stay as far from these hostile creatures as possible -with the exception of plague dragons, who have a natural immunity to serpenta venom. (Colored by autumnalis.)</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/16489_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Aer Phantom</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">While they appear non-threatening, dragons take care not to let this spectral creature pass through them.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/15298_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Agol</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">A backwards thinking creature.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13435_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Almandine Sturgeon</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Dwelling in the waters of the Crystal Pools has left the scales of this fish translucent and hard as a gemstone.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/376_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Amaranth Moth</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">This distinctive moth has deep reds and purples running through it's leafy wings. Its difficult to classify as purely flora or fauna.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13434_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Amber Gulper</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Sometimes dragon eats fish. Sometimes fish eats dragon.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/12739_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Amberwing Waveskimmer</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These avians are always humming. It's incredibly annoying.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
			</div>
	</div>
	</div>
<!--END CODEMEGEDDON-->

<!--End Main Content-->
</div>

	<!--Clear Floats-->
	<div class="clear"></div>

<!--End Content Container-->
</div>

<div style="width:auto; background-color:#731d08; padding-top:8px; padding-bottom:8px; height:90px;"><div style="margin-left:111px; width:728px; overflow:hidden;">

		<!-- Leaderboard -->
		<!--/* Zone www.flightrising.com Flight Rising - 728 x 90 Archive */-->
		<!--/* OpenX iFrame Tag v2.8.11 */-->

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456039264' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456039264' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456039264&amp;n=a26545c2' border='0' alt='' /></a></iframe>
		<script type='text/javascript' src='http://162.218.115.228/delivery/ag.php'></script>

		</div></div>
<!--End Bottom Banner-->
<div class="copybar">&copy; 2013 Stormlight Workshop. All Rights Reserved<br />
<a href="main.php?p=tos">Terms of Use</a> | <a href="http://flightrising.com/main.php?board=frd&id=749441&p=mb">Rules and Guidelines</a> | <a href="main.php?p=privacy">Privacy Policy</a> | <a href="main.php?p=credits">Credits</a> |  <a href="index.php?p=contact">Contact Us</a> | <a href="http://www.virtualpetlist.com/" target="_blank" alt="Virtual Pet List">Virtual Pets Forum</a></div>
<!--End Copybar-->

<!--End Container-->
</div>

<!-- Begin JQuery loading checks -->
<script type="text/javascript">
(function (){
	var args='';

	if (typeof jQuery == 'undefined') {
		// by definition, no jquery = no jquery UI
		args = 'nojquery=1&nojqueryui=1';
	} else if (typeof jQuery.ui == 'undefined') {
		// we have jquery, but no jquery UI
		args = 'nojqueryui=1';
	}

	function startCheckingForRecovery() {

		function recheck() {
			++counter;

			if (typeof jQuery != 'undefined' &&
				typeof jQuery.ui != 'undefined') {

				var img2 = new Image();
				img2.src = '/js_report.php?recovered=1&recover_time='+(counter*1000);

				clearInterval(intervalID);
			} else if (counter > 60) {
				clearInterval(intervalID);
			}
		}

		var counter=0;
		var intervalID = setInterval(recheck, 1000);

	}

	if (args != '') {
		var img = new Image();
		img.src = '/js_report.php?' + args;
		startCheckingForRecovery();
	}

})();
</script>
<!-- End JQuery loading checks -->

<!--ZENDESK TAB-->

</body>
</html>

"""