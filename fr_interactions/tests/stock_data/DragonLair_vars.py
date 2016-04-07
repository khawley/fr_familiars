DRAGON_LAIR_ID = "95470"
GEMSTONE_ID = "6930511"
GEMSTONE_FAMILIAR_ID = "7427"
UNNAMED_ID = "21304374"
DRAGON_LAIR_PAGE_1 = """
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
			sel.text = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=95470#"+id+"']"+quote+"[/quote]";
		}

		else
    	{  // Code for Mozilla Firefox
			var len = textarea.value.length;
	    	var start = textarea.selectionStart;
			var end = textarea.selectionEnd;


			var scrollTop = textarea.scrollTop;
			var scrollLeft = textarea.scrollLeft;


        	var sel = textarea.value.substring(start, end);
			var rep = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=95470#"+id+"']"+quote+"[/quote]";
        	textarea.value =  textarea.value.substring(0,start) + rep + textarea.value.substring(end,len);

			textarea.scrollTop = scrollTop;
			textarea.scrollLeft = scrollLeft;
		}
	}
</script>


	<script type="text/javascript">
	function randName(dragon,gen)
	{
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
	  if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
		document.getElementById("repname").innerHTML=xmlhttp.responseText;
		}
	  }
	xmlhttp.open("GET","includes/randnames.php?id="+dragon+"&gen="+gen,false);
	xmlhttp.send();
	}
	</script>


</head>





	<body style="background-image: url(/images/layout/arcane/bg.jpg); position:relative;">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/arcane/banner.jpg);">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	20:18    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">2775 Users Online</a></strong>
	</span>

	<!--Food-->
		<span id="food_bar">
	<span style="position:absolute; left:205px; bottom:2px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat insects.">
	<img src="/images/layout/icon_insect.png" width="26" height="20" border="0" align="absmiddle">
	291	</a>
	</span>

	<span style="position:absolute; left:305px; bottom:4px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat meat.">
	<img src="/images/layout/icon_meat.png" width="27" height="16" border="0" align="absmiddle">
	404	</a>
	</span>

	<span style="position:absolute; left:405px; bottom:3px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat seafood.">
	<img src="/images/layout/icon_seafood.png" width="24" height="18" border="0" align="absmiddle">
	340	</a>
	</span>

	<span style="position:absolute; left:505px; bottom:2px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat plants.">
	<img src="/images/layout/icon_plant.png" width="25" height="19" border="0" align="absmiddle">
	411	</a>
	</span>
	</span>
		<!--End Food-->



	<div style="position:absolute; bottom:2px; right:130px; cursor:pointer; height:20px;">
		<a id="messcnt" class="loginlinks loginbar" title="This shows how many new messages you have. Clicking this icon will take you directly to your inbox, where you can send and receive messages with other users." style="font-size:11px; cursor:pointer;" href="main.php?p=pm">
		<img id="messimg" src="../images/layout/small_message.png" width="30" height="20" align="absmiddle" border="0" />
		<span id="messalert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<div style="position:absolute; bottom:2px; right:70px; cursor:pointer; height:20px;">
		<a id="frensm" class="loginlinks loginbar" title="Click this icon to access your pending friend requests or view your friends list. You may accept or reject requests from this menu." style="font-size:11px; cursor:pointer;">
		<img id="frensimg" src="../images/layout/friends_icon.png" width="20" height="20" align="abstop" border="0" />
		<span id="frensalert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:absolute; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<div style="position:absolute; bottom:2px; right:10px; cursor:pointer; height:20px;">
		<a id="alertm" class="loginlinks loginbar" title="This lets you know how many new alerts you have. Clicking the Alerts icon will let you know about your recent clan and friend activity." style="font-size:11px; cursor:pointer;">
		<img id="alertimg" src="../images/layout/small_alert.png" width="23" height="20" align="absmiddle" border="0" />
		<span id="alert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<script type="text/javascript">
	$(document).mouseup(function (e){
		//var container = $("#alertwin");

		if (!$("#alertwin").is(e.target) && $("#alertwin").has(e.target).length === 0)
		{
			$("#alertwin").dialog('close');
			$('#alertwin').detach();
		}

		//var container2 = $("#logwin");

		if (!$("#logwin").is(e.target) && $("#logwin").has(e.target).length === 0)
		{
			$("#logwin").dialog('close');
			$('#logwin').detach();
		}


		if (!$("#frenswin").is(e.target) && $("#frenswin").has(e.target).length === 0)
		{
			$("#frenswin").dialog('close');
			$('#frenswin').detach();
		}

	});

	$("#alertm").click(function() {

		$('body').append('<div id="alertwin" style="display:none;"></div>');
		$("#alertwin").html('<img src="/images/layout/loading.gif"> loading...');

		$('#alertwin').dialog({
			title: "",
			width: 300,
			minHeight: 25,
			maxHeight: 200,
			modal:false,
			draggable:false,
			resizable:false,
			show: 'blind',
			position: {
				my: 'right top',
				at: 'right bottom',
				of: $('#alertimg')
			},
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
				$(".ui-dialog-titlebar", ui.dialog).hide();
			}
		});

		$('#alertwin').dialog('open');

		var data = '';
		$.ajax({
			type: "POST",
			data: data,
			url: "includes/ol/alerts.php",
			cache:false
		}).done(function(stuff){
			$("#alertwin").html(stuff);


			$.ajax({
				type: "POST",
				data: "",
				url: "includes/ol/alert_count.php",
				cache:false
			}).done(function(stuff){
				$("#alert").html(stuff);
			});


		});

	});

	$("#frensm").click(function() {

		$('body').append('<div id="frenswin" style="display:none;"></div>');
		$("#frenswin").html('<img src="/images/layout/loading.gif"> loading...');

		$('#frenswin').dialog({
			title: "",
			width: 300,
			minHeight: 25,
			maxHeight: 200,
			modal:false,
			draggable:false,
			resizable:false,
			show: 'blind',
			position: {
				my: 'right top',
				at: 'right bottom',
				of: $('#frensimg')
			},
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
				$(".ui-dialog-titlebar", ui.dialog).hide();
			}
		});

		$('#frenswin').dialog('open');

		var data = '';
		$.ajax({
			type: "POST",
			data: data,
			url: "includes/ol/frensreq.php",
			cache:false
		}).done(function(stuff){
			$("#frenswin").html(stuff);
		});

	});

	</script>
	<!--<div id="alertwin" style="display:none;"></div>	-->
	<!--<div id="frenswin" style="display:none;"></div>	-->

</div>

</div>

	<div id="ticker" style="position:absolute; background-image:url(/images/layout/ticker_topbar.png); right:0px; top:0px; height:24px; width:285px; font-size:10px; color:#393939; overflow:hidden;">

			<div class="rotating-item" id="tick1" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/achievement.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=achieve">Earn achievements as your clan grows.</a>
		</div>
				<div class="rotating-item" id="tick2" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/feed.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=gather">Well-fed clans earn daily bonuses.</a>
		</div>
				<div class="rotating-item" id="tick3" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/Bug.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=mb&board=bug">Found a bug? Tell us about it!</a>
		</div>
				<div class="rotating-item" id="tick4" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/heart_big.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=bestiary">Bond with your familiars daily for rewards.</a>
		</div>
				<div class="rotating-item" id="tick5" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/tumblr.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.tumblr.com/">Follow Flight Rising on Tumblr</a>
		</div>
				<div class="rotating-item" id="tick6" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/deviant.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.deviantart.com/">Flight Rising Deviantart: Share Your Art!</a>
		</div>
				<div class="rotating-item" id="tick7" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/tomo.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=tradepost&lot=trivia">Test your trivia skills with Tomo!</a>
		</div>
				<div class="rotating-item" id="tick8" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/status.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/site/status">Keep up to date on the status of FR!</a>
		</div>
				<div class="rotating-item" id="tick9" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/15573.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1704902">Thylacine tertiary gene discovered.</a>
		</div>
				<div class="rotating-item" id="tick10" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/swipp2.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1623317">Meet Pipp and Tripp at the Swap Stand!</a>
		</div>
				<div class="rotating-item" id="tick11" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/15702.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1716128">Sylvan apparel is now stocking.</a>
		</div>
				<div class="rotating-item" id="tick12" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/rainbowscarf2.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=market&type=1&tab=app">Prismatic Silks are now available.</a>
		</div>
				<div class="rotating-item" id="tick13" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/familiarcontest.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1749772">Familiar coloring contest results are in!</a>
		</div>
				<div class="rotating-item" id="tick14" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/16004.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1734727">Stained: new tertiary gene now available.</a>
		</div>
				<div class="rotating-item" id="tick15" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/7.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="main.php?p=dominance">The Shadow flight is dominating!</a>
		</div>

	</div>
	<script type="text/javascript">

	$(window).load(function() { //start after HTML, images have loaded
		var InfiniteRotator =
		{
			init: function()
			{
				//initial fade-in time (in milliseconds)
				var initialFadeIn = 1000;
				//interval between items (in milliseconds)
				var itemInterval = 13000;
				//cross-fade time (in milliseconds)
				var fadeTime = 2500;
				//count number of items
				var numberOfItems = $('.rotating-item').length;
				//set current item
				var currentItem = 0;
				//show first item
				$('.rotating-item').eq(currentItem).fadeIn(initialFadeIn);
				//loop through the items
				var infiniteLoop = setInterval(function(){
					$('.rotating-item').eq(currentItem).fadeOut(fadeTime);

					if(currentItem == numberOfItems -1){
						currentItem = 0;
					}else{
						currentItem++;
					}
					$('.rotating-item').eq(currentItem).fadeIn(fadeTime);

				}, itemInterval);
			}
		};

		InfiniteRotator.init();

	});
	</script>

<div id="usertab" style="position:absolute; background-image:url(/images/layout/user_module_bg.png); right:0px; bottom:31px; height:112px; width:285px;">
	<span style="width:60px; height:60px; display:inline-block; position:absolute; top:10px; left:10px; background-color:#FFF;" id="ltavtr">
		<a href="main.php?p=lair&tab=userpage&id=95470"><img src="/rendern/portraits/71663/7166200p.png?mtime=VN2ddAAANvE" height="60" width="60" style="border:1px solid #000;" /></a>
	</span>

			<span style="width:60px; height:60px; display:inline-block; position:absolute; top:71px; left:10px;">
			<img src="/images/layout/elemental_banners/arcane_banner.png" height="60" width="60" />
		</span>
			<span style="width:185px; height:20px; display:inline-block; position:absolute; top:7px; left:85px; ">
		<a href="main.php?p=lair&tab=userpage&id=95470"><span style="color:#731d08; font-size:15px; font-weight:bold;">slaynsoul</span></a>
		<img src="../images/icons/down_arrow.png" width="15" height="15" id="logbutton" style="vertical-align:text-bottom; cursor:pointer;" />

		<script type="text/javascript">

		$("#logbutton").click(function() {
			$('body').append('<div id="logwin" style="display:none;"></div>');
			$("#logwin").html('<img src="/images/layout/loading.gif"> loading...');

			$('#logwin').dialog({
				title: "",
				width: 135,
				minHeight: 25,
				maxHeight: 200,
				modal:false,
				draggable:false,
				resizable:false,
				show: 'blind',
				position: {
					my: 'left top',
					at: 'left top',
					of: $('#logbutton')
				},
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
					$(".ui-dialog-titlebar", ui.dialog).hide();
				}
			});

			$('#logwin').dialog('open');

			$.ajax({
				type: "POST",
				data: '',
				url: "includes/ol/user_window.php",
				cache:false
			}).done(function(stuff){
				$("#logwin").html(stuff);
			});

		});



		</script>


	</span>



	<span style="text-align:left; cursor:default; position:absolute; left:210px; bottom:3px;">
		<a class="loginlinks loginbar" title="Achievements are earned by completing specific and sometimes difficult tasks." style="color:#731d08;" href="main.php?p=achieve">
		<span id="login_ach" style="position:relative; height:25px; width:25px; display:inline-block;">
			<img src="/images/layout/icon_achievements.png" width="25" height="25" border="0" align="absmiddle" style="position:absolute; right:0px; bottom:0px; z-index:20;" id="overlay_ach">
			<img src="/images/layout/icon_achievements.png" width="25" height="25" border="0" align="absmiddle">
		</span>

		<span style="font-size:11px;">
		1095		</span>
		</a>
	</span>



	<span style="position:absolute; left:210px; top:57px; text-align:left;" id="bstcount">

	<a class="loginlinks loginbar" style="color:#731d08; font-size:11px;" title="This shows how many familiars your clan has befriended. This number increases with each unique new familiar you have in your hoard or accompanying your dragons. Clicking this icon will take you directly to your Bestiary." href="main.php?p=bestiary">
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 359	</a>

	</span>



	<span style="position:absolute; left:85px; display:inline-block; top:28px; width:185px; height:26px;">
    <a rel="includes/ol/nrg_tooltip.php?percent=100&wellfed=3" class="clue_nrg">

    <div style="position:absolute; top:0px; left:0px; width:185px; background-image:url(images/bars/avg_back.png); height:20px;">
    	<span style="position:absolute; text-shadow: 0 0 0.2em #FFF, 0 0 0.2em #FFF, 0 0 0.2em #FFF; margin-top:2px; text-align:center; font-weight:bold; width:180px; margin-right:auto; margin-left:auto; z-index:2;">100%</span>
    	<div style="width:185px; overflow:hidden; position:relative; background-image:url(images/bars/avg_energy.png); height:20px;">
		</div>
    </div>

    <img style="position:absolute; top:20px; left:0px;" border="0" src="/images/bars/day3bar.png" width="185" height="6" />

    </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; top:60px;" >
		<a class="loginbar loginlinks" title="This is how much treasure you have collected in your lair." onclick="window.location='main.php?p=hoard'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_treasure.png" border="0" align="absmiddle">

                	<span id="user_treasure" style="font-size:11px;">1372272</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3068</span>
		</a>
		<!--<input style="width:40px; height:20px; font-size:10px; font-weight:bold; color:#000; background-color:#f4f4f4; border:solid 1px #000; -moz-border-radius:0.4em; -khtml-border-radius:0.4em; -webkit-border-radius:0.4em; border-radius:0.4em;" type="button" name="refill" value="Add" onclick="window.location='main.php?p=ge'" />-->
	</span>
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

	<a href="main.php?p=clanhome"><img src="/images/layout/header_clan.png" border="0" width="179" height="29" onMouseOver="this.src=clan_hover.src" onMouseOut="this.src='/images/layout/header_clan.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=lair&id=95470"><span class="navbar-glow-hover">Dragon Lair</span></a>
	<a class="navbar" href="main.php?p=lair&id=95470&tab=hatchery"><span class="navbar-glow-hover">Nesting Grounds</span></a>

	<span style="position:relative; display:inline-block">
	<a class="navbar" href="main.php?p=gather"><span class="navbar-glow-hover">Gather Items</span></a>




	</span>

	<a class="navbar" href="main.php?p=lair&tab=userpage&id=95470"><span class="navbar-glow-hover">Clan Profile</span></a>
	<a class="navbar" href="main.php?p=hoard"><span class="navbar-glow-hover">Hoard</span></a>
	<a class="navbar" href="main.php?p=bestiary"><span class="navbar-glow-hover">Bestiary</span></a>
	<a class="navbar" href="main.php?p=pm"><span class="navbar-glow-hover">Messages</span></a>

	<a href="main.php?p=shophome"><img src="/images/layout/header_shop.png" border="0" width="179" height="29" onMouseOver="this.src=shop_hover.src" onMouseOut="this.src='/images/layout/header_shop.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=ge"><span class="navbar-glow-hover">Purchase Gems</span></a>
	<a class="navbar" href="main.php?p=market"><span class="navbar-glow-hover">Marketplace</span></a>
	<a class="navbar" href="main.php?p=ah"><span class="navbar-glow-hover">Auction House</span></a>
	<a class="navbar" href="main.php?p=tradepost"><span class="navbar-glow-hover">Trading Post</span></a>
	<a class="navbar" href="main.php?p=crossroads"><span class="navbar-glow-hover">Crossroads</span></a>
	<a class="navbar" href="main.php?p=skins"><span class="navbar-glow-hover">Custom Skins</span></a>		<a class="navbar" href="main.php?p=festive"><span class="navbar-glow-hover">Festive Favors</span></a>

	<a href="main.php?p=playhome"><img src="/images/layout/header_play.png" border="0" width="179" height="29" onMouseOver="this.src=play_hover.src" onMouseOut="this.src='/images/layout/header_play.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=faire"><span class="navbar-glow-hover">Fairgrounds</span></a>
	<a class="navbar" href="main.php?p=coliseum"><span class="navbar-glow-hover">Coliseum</span></a>
		<a class="navbar" href="main.php?p=dominance"><span class="navbar-glow-hover">Dominance</span></a>
	<!--<a class="navbar" href="#">Adventure</a>-->

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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456201096' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456201096' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456201096&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
<img src="/images/layout/arcane/internal_bg.jpg" style="position:absolute; right:0px;" />
<div style="position:relative; width:730px; margin:10px;" id="super-container">
	<script type="text/javascript">
	function ValidateLair(form)
	{
		var valid = 0;

		if (form.dragon.checked == false) {
		valid++;
		alert ('Please check "Accept" to verify that you want to do this.');
		return false;
		}

		if (valid < 1) {
			form.submit();
		}
	}
	</script>

	<a title="Click here to learn more about this page." class="cluehelp"><img src="/images/layout/icon_help.png" style="position:absolute; right:0px; top:0px; z-index:10px; cursor:pointer;" onclick="helpMe('lair')" /></a>

		<div style="font-size:12px; color:#000;">
			<a href="main.php?p=clanhome" style="color:#000">Clan Home</a> &raquo;
		<a href="main.php?p=lair&tab=userpage&id=95470" style=" color:#000;">Clan Profile</a> |
		<a href="main.php?p=lair&id=95470" style=" color:#731d08; font-weight:bold;">Dragon Lair</a> |
		<span style="position:relative; display:inline-block;"><a href="main.php?p=lair&tab=hatchery&id=95470" style=" color:#000;">Nesting Grounds</a>


		</span>
			</div>



	<div style="position:relative; text-align:right; width:705px; height:69px;">

			<a href="main.php?p=clanhome"><img border="0" src="/images/layout/button_back.png" style="position:absolute; top:25px; left:15px; border: 0px;"></a>

	<span style="font-size:22px; text-align:left; color:#731d08; font-weight:bold; position:absolute; top:20px; left:52px;">
	slaynsoul's Dragons		<div style="width:390px; font-size:12px; color:#999; font-weight:normal;">
		Manage and feed the dragons of your clan.
		</div>
			</span>



			<span style="position:absolute; bottom:10px; right:0px;">

			<span style="margin-right:10px;">
			<a href="main.php?p=lairorder"><img src="/images/layout/button_arrange.png" border="0" /></a>
			</span>
		<script type="text/javascript">

		function feedAll()
		{
			$('body').append('<div id="feeder"></div>');
			$("#feeder").html('<img src="/images/layout/loading.gif"> loading...');
			$('#feeder').dialog({
				autoOpen: false,
				title: "Feed Dragons",
				width: 350,
				height: 190,
				modal: true,
				resizable: false,
				draggable: false,
				closeOnEscape: false,
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
				}
			});
			$('#feeder').dialog('open');

			$.ajax({
				type: "POST",
				data: "",
				url: "includes/ol/feed.php",
				cache:false
			}).done(function(stuff){
				$("#feeder").html(stuff);
			});
		}
		</script>

		<span style="position:relative; display:inline-block;">
		<img src="/images/layout/button_feed.png" border="0" onclick="feedAll()" id="feedall" style="cursor:pointer;" />


		</span>
		<!--<input type="button" value="PRESS HERE TO FEED DRAGONS" onclick="feedAll()" id="feedall" class="mb_button" style="font-size:11px; cursor:pointer; color:#fff; background-color:#731d08; height:25px;" />-->
		<!--<a class="treeNode_default" style="font-size:11px; cursor:pointer;" id="feedall" onclick="feedAll()">Feed All Dragons</a>-->

		</span>

</span>
	</div>


	<div id="tunak" style="display:none;"></div>

	<!--<div id="paging" style="width:700px; text-align:left; line-height:30px; margin-left:15px;">-->
		<div style="width:650px; height:27px; font-size:12px; text-align:center; margin-bottom:10px; margin-left:auto; margin-right:auto;"><img border="0" src="/images/layout/arrow_left_off.png" style="vertical-align:middle; position:absolute; left:25px;" /> <span style="font-weight:bold;">1</span> <a href='main.php?p=lair&id=95470&page=2'>2</a> <a href='main.php?p=lair&id=95470&page=3'>3</a> <a href='main.php?p=lair&id=95470&page=4'>4</a> <a href='main.php?p=lair&id=95470&page=5'>5</a> <a href='main.php?p=lair&id=95470&page=6'>6</a> <a href='main.php?p=lair&id=95470&page=7'>7</a> <a href='main.php?p=lair&id=95470&page=2'><img border="0" src="/images/layout/arrow_right.png" style="cursor:pointer; vertical-align:middle; position:absolute; right:25px;" /></a> </div>
	<!--</div>-->

	<FORM METHOD="POST" ACTION="main.php?p=lair">
      <div style="width:700px; margin-left:auto; margin-right:auto;">
      <!-- ADDITIONAL DRAGONS -->
            		<ul id="nomove" class="nomove">
        					<li class="nomove" dragonid="1">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Gemstone
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('6930511')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=6930511" style="border:none" rel="includes/dragonajax.php?id=6930511" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/69306/6930511.png?mtime=VTWbIwAAPUQ" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_9.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 15 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Female Dragon">
						<img src="/images/icons/small_female.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="2">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Terrorbone
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('6930512')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=6930512" style="border:none" rel="includes/dragonajax.php?id=6930512" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/69306/6930512.png?mtime=VUKmQAAARQc" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_9.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 15 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="3">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Sapphiredge
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7137149')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7137149" style="border:none" rel="includes/dragonajax.php?id=7137149" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/71372/7137149.png?mtime=VN2YdwAAVBs" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_2.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 29 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="4">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Kala
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7166200')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7166200" style="border:none" rel="includes/dragonajax.php?id=7166200" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/71663/7166200.png?mtime=VN2ddAAATtY" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_2.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 11 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Female Dragon">
						<img src="/images/icons/small_female.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="5">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Dalthor
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('6849422')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=6849422" style="border:none" rel="includes/dragonajax.php?id=6849422" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/68495/6849422.png?mtime=VNRD5QAATNY" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_8.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 24 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="6">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">AmethystDream
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7052976')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7052976" style="border:none" rel="includes/dragonajax.php?id=7052976" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/70530/7052976.png?mtime=VN2W7AAAVjk" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_5.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 24 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Female Dragon">
						<img src="/images/icons/small_female.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="7">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Latte
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('8997353')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=8997353" style="border:none" rel="includes/dragonajax.php?id=8997353" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/89974/8997353.png?mtime=VQ8Z4QAASnM" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_2.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 6 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Female Dragon">
						<img src="/images/icons/small_female.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="8">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Midnight
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('9154109')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=9154109" style="border:none" rel="includes/dragonajax.php?id=9154109" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/91542/9154109.png?mtime=Vp-rAwAARcs" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_9.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 6 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="9">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Rin
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('10596314')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=10596314" style="border:none" rel="includes/dragonajax.php?id=10596314" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/105964/10596314.png?mtime=VOQY1AAAUEU" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_3.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 14 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Female Dragon">
						<img src="/images/icons/small_female.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="10">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Tyrell
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7484548')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7484548" style="border:none" rel="includes/dragonajax.php?id=7484548" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/74846/7484548.png?mtime=VLqkbAAASR8" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_5.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 14 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="11">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Cornflower
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7170024')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7170024" style="border:none" rel="includes/dragonajax.php?id=7170024" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/71701/7170024.png?mtime=VOUDAwAAUvs" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_4.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 1 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="12">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">CrystalGaze
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7341585')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7341585" style="border:none" rel="includes/dragonajax.php?id=7341585" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/73416/7341585.png?mtime=VNBBSwAAQYo" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_3.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 1 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Female Dragon">
						<img src="/images/icons/small_female.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="13">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">Ihimaera
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7126756')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7126756" style="border:none" rel="includes/dragonajax.php?id=7126756" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/71268/7126756.png?mtime=VNBCZgAAP48" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_11.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="14">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">MistFall
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('7302345')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=7302345" style="border:none" rel="includes/dragonajax.php?id=7302345" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/73024/7302345.png?mtime=VNBB9gAAQsY" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_10.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
													<a class="miniclue" TITLE="Female Dragon">
						<img src="/images/icons/small_female.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
								<li class="nomove" dragonid="15">
				<div class="dragoncard">
					<div style="background-image:url(images/layout/dragoncards/bg_top_noshadow.jpg); height:126px;">
						<div style="color:#731d08; font-weight:bold; text-align:center; margin-top:5px;">WinterBone
                                                	<img src="../images/layout/refresh.png" title="Regenerate Images" width="12" height="12" onClick="imageKill('8565454')" style="margin-left:10px; cursor:pointer;">

                        </div>

						<div style="margin-top:4px; margin-bottom:4px;">
													<a href="main.php?p=lair&id=95470&tab=dragon&did=8565454" style="border:none" rel="includes/dragonajax.php?id=8565454" class="clue">
							<img class="dragonthmb" src="/rendern/avatars/85655/8565454.png?mtime=VJLN8wAAW4A" border="0"

							height="100" width="100"							>
							</a>
						</div>

					</div>

					<div style="background-image:url(images/layout/dragoncards/element_9.jpg); height:51px;">


                        						<div style="margin-bottom:10px; margin-top:4px; margin-left:auto; margin-right:auto; background-image:url(images/bars/small_back.png); height:10px; width:106px; position:relative;">
							<!--<span style="position:absolute; text-shadow: 0 0 0.3em #000, 0 0 0.3em #000, 0 0 0.3em #000; left:0px; top:0px; text-align:center; font-weight:bold; width:106px; margin-right:auto; margin-left:auto; z-index:2; font-size:9px;"></span>-->
                            <img src="../images/layout/trans.png" height="10" width="106" TITLE="50 / 50" alt="50 / 50" style="position:absolute; z-index:2; left:0px; top:0px;">
							<div style="width:106px; overflow:hidden; position:relative; background-image:url(images/bars/small_energy.png); height:10px; z-index:1;"></div>
						</div>

						<div style="text-align:right; margin-right:10px;">

													<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>
														<a class="loginbar" TITLE="This dragon will not be available to breed for 11 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
													<a class="miniclue" TITLE="Male Dragon">
						<img src="/images/icons/small_male.png" >
						</a>
						</div>
					</div>

				</div>
				</li>
				              </ul>
            <div style="clear: left;"></div>

      <!--END ADDITIONAL DRAGONS -->

	</div>
</form>

<script type="text/javascript">
function babyName(id, str)
{
	$.ajax({
		type: "POST",
		data: {id: id, name: str},
		url: "includes/ol/babynames.php",
		cache:false
	}).done(function(stuff){
		$("#naming").html(stuff);

		$('#naming').dialog({
			autoOpen: false,
			title: "Name Dragon",
			width: 375,
			height: 180,
			modal: true,
			resizable: false,
			draggable: false
		});

		$('#naming').dialog('open');

	});
}
</script>

    <script type="text/javascript">
	function imageKill(id)
	{
		$('body').append('<div id="imgkill"></div>');
		$("#imgkill").html('<img src="/images/layout/loading.gif"> loading...');

		$('#imgkill').dialog({
			autoOpen: false,
			title: "Regenerate Images",
			width: 300,
			height: "auto",
			modal: true,
			resizable: false,
			draggable: false,
			closeOnEscape: false,
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
			}
		});

		$('#imgkill').dialog('open');

		$.ajax({
			type: "POST",
			data: {did: id},
			url: "includes/ol/imgkill.php",
			cache:false
		}).done(function(stuff){
			$("#imgkill").html(stuff);
		});
	}
	</script>

<div id="naming"></div>



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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456201096' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456201096' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456201096&amp;n=a26545c2' border='0' alt='' /></a></iframe>
		<script type='text/javascript' src='http://162.218.115.228/delivery/ag.php'></script>

		</div></div>
<!--End Bottom Banner-->
<div class="copybar">&copy; 2013 Stormlight Workshop. All Rights Reserved<br />
<a href="main.php?p=tos">Terms of Use</a> | <a href="http://flightrising.com/main.php?board=frd&id=749441&p=mb">Rules and Guidelines</a> | <a href="main.php?p=privacy">Privacy Policy</a> | <a href="main.php?p=credits">Credits</a> |  <a href="index.php?p=contact">Contact Us</a> | <a href="http://www.virtualpetlist.com/" target="_blank" alt="Virtual Pet List">Virtual Pets Forum</a></div>
<!--End Copybar-->

<!--End Container-->
</div>

	<script type="text/javascript">
	</script>

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

DRAGONS_FROM_LAIR_PAGE_1 = ""

DRAGON_PAGE_GEMSTONE = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta property="og:title" content="slaynsoul's dragon Gemstone - Breed, raise, and train dragons on Flight Rising!"/>
	<meta property="og:type" content="website"/>
	<meta property="og:image" content="/rendern/350/69306/6930511_350.png?mtime=VTWbIwACAqc"/>
	<meta property="og:url" content="http://flightrising.com/main.php?dragon=6930511"/>
	<meta property="og:site_name" content="Flight Rising"/>
	<meta property="fb:admins" content="548611600" />
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
			sel.text = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=95470#"+id+"']"+quote+"[/quote]";
		}

		else
    	{  // Code for Mozilla Firefox
			var len = textarea.value.length;
	    	var start = textarea.selectionStart;
			var end = textarea.selectionEnd;


			var scrollTop = textarea.scrollTop;
			var scrollLeft = textarea.scrollLeft;


        	var sel = textarea.value.substring(start, end);
			var rep = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=95470#"+id+"']"+quote+"[/quote]";
        	textarea.value =  textarea.value.substring(0,start) + rep + textarea.value.substring(end,len);

			textarea.scrollTop = scrollTop;
			textarea.scrollLeft = scrollLeft;
		}
	}
</script>


	<script type="text/javascript">
	function randName(dragon,gen)
	{
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
	  if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
		document.getElementById("repname").innerHTML=xmlhttp.responseText;
		}
	  }
	xmlhttp.open("GET","includes/randnames.php?id="+dragon+"&gen="+gen,false);
	xmlhttp.send();
	}
	</script>


</head>





	<body style="background-image: url(/images/layout/arcane/bg.jpg); position:relative;">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/arcane/banner.jpg);">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	21:25    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">2385 Users Online</a></strong>
	</span>

	<!--Food-->
		<span id="food_bar">
	<span style="position:absolute; left:205px; bottom:2px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat insects.">
	<img src="/images/layout/icon_insect.png" width="26" height="20" border="0" align="absmiddle">
	291	</a>
	</span>

	<span style="position:absolute; left:305px; bottom:4px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat meat.">
	<img src="/images/layout/icon_meat.png" width="27" height="16" border="0" align="absmiddle">
	404	</a>
	</span>

	<span style="position:absolute; left:405px; bottom:3px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat seafood.">
	<img src="/images/layout/icon_seafood.png" width="24" height="18" border="0" align="absmiddle">
	340	</a>
	</span>

	<span style="position:absolute; left:505px; bottom:2px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat plants.">
	<img src="/images/layout/icon_plant.png" width="25" height="19" border="0" align="absmiddle">
	411	</a>
	</span>
	</span>
		<!--End Food-->



	<div style="position:absolute; bottom:2px; right:130px; cursor:pointer; height:20px;">
		<a id="messcnt" class="loginlinks loginbar" title="This shows how many new messages you have. Clicking this icon will take you directly to your inbox, where you can send and receive messages with other users." style="font-size:11px; cursor:pointer;" href="main.php?p=pm">
		<img id="messimg" src="../images/layout/small_message.png" width="30" height="20" align="absmiddle" border="0" />
		<span id="messalert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<div style="position:absolute; bottom:2px; right:70px; cursor:pointer; height:20px;">
		<a id="frensm" class="loginlinks loginbar" title="Click this icon to access your pending friend requests or view your friends list. You may accept or reject requests from this menu." style="font-size:11px; cursor:pointer;">
		<img id="frensimg" src="../images/layout/friends_icon.png" width="20" height="20" align="abstop" border="0" />
		<span id="frensalert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:absolute; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<div style="position:absolute; bottom:2px; right:10px; cursor:pointer; height:20px;">
		<a id="alertm" class="loginlinks loginbar" title="This lets you know how many new alerts you have. Clicking the Alerts icon will let you know about your recent clan and friend activity." style="font-size:11px; cursor:pointer;">
		<img id="alertimg" src="../images/layout/small_alert.png" width="23" height="20" align="absmiddle" border="0" />
		<span id="alert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<script type="text/javascript">
	$(document).mouseup(function (e){
		//var container = $("#alertwin");

		if (!$("#alertwin").is(e.target) && $("#alertwin").has(e.target).length === 0)
		{
			$("#alertwin").dialog('close');
			$('#alertwin').detach();
		}

		//var container2 = $("#logwin");

		if (!$("#logwin").is(e.target) && $("#logwin").has(e.target).length === 0)
		{
			$("#logwin").dialog('close');
			$('#logwin').detach();
		}


		if (!$("#frenswin").is(e.target) && $("#frenswin").has(e.target).length === 0)
		{
			$("#frenswin").dialog('close');
			$('#frenswin').detach();
		}

	});

	$("#alertm").click(function() {

		$('body').append('<div id="alertwin" style="display:none;"></div>');
		$("#alertwin").html('<img src="/images/layout/loading.gif"> loading...');

		$('#alertwin').dialog({
			title: "",
			width: 300,
			minHeight: 25,
			maxHeight: 200,
			modal:false,
			draggable:false,
			resizable:false,
			show: 'blind',
			position: {
				my: 'right top',
				at: 'right bottom',
				of: $('#alertimg')
			},
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
				$(".ui-dialog-titlebar", ui.dialog).hide();
			}
		});

		$('#alertwin').dialog('open');

		var data = '';
		$.ajax({
			type: "POST",
			data: data,
			url: "includes/ol/alerts.php",
			cache:false
		}).done(function(stuff){
			$("#alertwin").html(stuff);


			$.ajax({
				type: "POST",
				data: "",
				url: "includes/ol/alert_count.php",
				cache:false
			}).done(function(stuff){
				$("#alert").html(stuff);
			});


		});

	});

	$("#frensm").click(function() {

		$('body').append('<div id="frenswin" style="display:none;"></div>');
		$("#frenswin").html('<img src="/images/layout/loading.gif"> loading...');

		$('#frenswin').dialog({
			title: "",
			width: 300,
			minHeight: 25,
			maxHeight: 200,
			modal:false,
			draggable:false,
			resizable:false,
			show: 'blind',
			position: {
				my: 'right top',
				at: 'right bottom',
				of: $('#frensimg')
			},
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
				$(".ui-dialog-titlebar", ui.dialog).hide();
			}
		});

		$('#frenswin').dialog('open');

		var data = '';
		$.ajax({
			type: "POST",
			data: data,
			url: "includes/ol/frensreq.php",
			cache:false
		}).done(function(stuff){
			$("#frenswin").html(stuff);
		});

	});

	</script>
	<!--<div id="alertwin" style="display:none;"></div>	-->
	<!--<div id="frenswin" style="display:none;"></div>	-->

</div>

</div>

	<div id="ticker" style="position:absolute; background-image:url(/images/layout/ticker_topbar.png); right:0px; top:0px; height:24px; width:285px; font-size:10px; color:#393939; overflow:hidden;">

			<div class="rotating-item" id="tick1" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/achievement.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=achieve">Earn achievements as your clan grows.</a>
		</div>
				<div class="rotating-item" id="tick2" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/feed.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=gather">Well-fed clans earn daily bonuses.</a>
		</div>
				<div class="rotating-item" id="tick3" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/Bug.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=mb&board=bug">Found a bug? Tell us about it!</a>
		</div>
				<div class="rotating-item" id="tick4" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/heart_big.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=bestiary">Bond with your familiars daily for rewards.</a>
		</div>
				<div class="rotating-item" id="tick5" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/tumblr.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.tumblr.com/">Follow Flight Rising on Tumblr</a>
		</div>
				<div class="rotating-item" id="tick6" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/deviant.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.deviantart.com/">Flight Rising Deviantart: Share Your Art!</a>
		</div>
				<div class="rotating-item" id="tick7" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/tomo.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=tradepost&lot=trivia">Test your trivia skills with Tomo!</a>
		</div>
				<div class="rotating-item" id="tick8" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/status.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/site/status">Keep up to date on the status of FR!</a>
		</div>
				<div class="rotating-item" id="tick9" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/15573.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1704902">Thylacine tertiary gene discovered.</a>
		</div>
				<div class="rotating-item" id="tick10" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/swipp2.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1623317">Meet Pipp and Tripp at the Swap Stand!</a>
		</div>
				<div class="rotating-item" id="tick11" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/15702.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1716128">Sylvan apparel is now stocking.</a>
		</div>
				<div class="rotating-item" id="tick12" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/rainbowscarf2.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=market&type=1&tab=app">Prismatic Silks are now available.</a>
		</div>
				<div class="rotating-item" id="tick13" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/familiarcontest.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1749772">Familiar coloring contest results are in!</a>
		</div>
				<div class="rotating-item" id="tick14" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/16004.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1734727">Stained: new tertiary gene now available.</a>
		</div>
				<div class="rotating-item" id="tick15" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/7.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="main.php?p=dominance">The Shadow flight is dominating!</a>
		</div>

	</div>
	<script type="text/javascript">

	$(window).load(function() { //start after HTML, images have loaded
		var InfiniteRotator =
		{
			init: function()
			{
				//initial fade-in time (in milliseconds)
				var initialFadeIn = 1000;
				//interval between items (in milliseconds)
				var itemInterval = 13000;
				//cross-fade time (in milliseconds)
				var fadeTime = 2500;
				//count number of items
				var numberOfItems = $('.rotating-item').length;
				//set current item
				var currentItem = 0;
				//show first item
				$('.rotating-item').eq(currentItem).fadeIn(initialFadeIn);
				//loop through the items
				var infiniteLoop = setInterval(function(){
					$('.rotating-item').eq(currentItem).fadeOut(fadeTime);

					if(currentItem == numberOfItems -1){
						currentItem = 0;
					}else{
						currentItem++;
					}
					$('.rotating-item').eq(currentItem).fadeIn(fadeTime);

				}, itemInterval);
			}
		};

		InfiniteRotator.init();

	});
	</script>

<div id="usertab" style="position:absolute; background-image:url(/images/layout/user_module_bg.png); right:0px; bottom:31px; height:112px; width:285px;">
	<span style="width:60px; height:60px; display:inline-block; position:absolute; top:10px; left:10px; background-color:#FFF;" id="ltavtr">
		<a href="main.php?p=lair&tab=userpage&id=95470"><img src="/rendern/portraits/71663/7166200p.png?mtime=VN2ddAAANvE" height="60" width="60" style="border:1px solid #000;" /></a>
	</span>

			<span style="width:60px; height:60px; display:inline-block; position:absolute; top:71px; left:10px;">
			<img src="/images/layout/elemental_banners/arcane_banner.png" height="60" width="60" />
		</span>
			<span style="width:185px; height:20px; display:inline-block; position:absolute; top:7px; left:85px; ">
		<a href="main.php?p=lair&tab=userpage&id=95470"><span style="color:#731d08; font-size:15px; font-weight:bold;">slaynsoul</span></a>
		<img src="../images/icons/down_arrow.png" width="15" height="15" id="logbutton" style="vertical-align:text-bottom; cursor:pointer;" />

		<script type="text/javascript">

		$("#logbutton").click(function() {
			$('body').append('<div id="logwin" style="display:none;"></div>');
			$("#logwin").html('<img src="/images/layout/loading.gif"> loading...');

			$('#logwin').dialog({
				title: "",
				width: 135,
				minHeight: 25,
				maxHeight: 200,
				modal:false,
				draggable:false,
				resizable:false,
				show: 'blind',
				position: {
					my: 'left top',
					at: 'left top',
					of: $('#logbutton')
				},
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
					$(".ui-dialog-titlebar", ui.dialog).hide();
				}
			});

			$('#logwin').dialog('open');

			$.ajax({
				type: "POST",
				data: '',
				url: "includes/ol/user_window.php",
				cache:false
			}).done(function(stuff){
				$("#logwin").html(stuff);
			});

		});



		</script>


	</span>



	<span style="text-align:left; cursor:default; position:absolute; left:210px; bottom:3px;">
		<a class="loginlinks loginbar" title="Achievements are earned by completing specific and sometimes difficult tasks." style="color:#731d08;" href="main.php?p=achieve">
		<span id="login_ach" style="position:relative; height:25px; width:25px; display:inline-block;">
			<img src="/images/layout/icon_achievements.png" width="25" height="25" border="0" align="absmiddle" style="position:absolute; right:0px; bottom:0px; z-index:20;" id="overlay_ach">
			<img src="/images/layout/icon_achievements.png" width="25" height="25" border="0" align="absmiddle">
		</span>

		<span style="font-size:11px;">
		1095		</span>
		</a>
	</span>



	<span style="position:absolute; left:210px; top:57px; text-align:left;" id="bstcount">

	<a class="loginlinks loginbar" style="color:#731d08; font-size:11px;" title="This shows how many familiars your clan has befriended. This number increases with each unique new familiar you have in your hoard or accompanying your dragons. Clicking this icon will take you directly to your Bestiary." href="main.php?p=bestiary">
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 359	</a>

	</span>



	<span style="position:absolute; left:85px; display:inline-block; top:28px; width:185px; height:26px;">
    <a rel="includes/ol/nrg_tooltip.php?percent=100&wellfed=3" class="clue_nrg">

    <div style="position:absolute; top:0px; left:0px; width:185px; background-image:url(images/bars/avg_back.png); height:20px;">
    	<span style="position:absolute; text-shadow: 0 0 0.2em #FFF, 0 0 0.2em #FFF, 0 0 0.2em #FFF; margin-top:2px; text-align:center; font-weight:bold; width:180px; margin-right:auto; margin-left:auto; z-index:2;">100%</span>
    	<div style="width:185px; overflow:hidden; position:relative; background-image:url(images/bars/avg_energy.png); height:20px;">
		</div>
    </div>

    <img style="position:absolute; top:20px; left:0px;" border="0" src="/images/bars/day3bar.png" width="185" height="6" />

    </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; top:60px;" >
		<a class="loginbar loginlinks" title="This is how much treasure you have collected in your lair." onclick="window.location='main.php?p=hoard'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_treasure.png" border="0" align="absmiddle">

                	<span id="user_treasure" style="font-size:11px;">1378362</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3068</span>
		</a>
		<!--<input style="width:40px; height:20px; font-size:10px; font-weight:bold; color:#000; background-color:#f4f4f4; border:solid 1px #000; -moz-border-radius:0.4em; -khtml-border-radius:0.4em; -webkit-border-radius:0.4em; border-radius:0.4em;" type="button" name="refill" value="Add" onclick="window.location='main.php?p=ge'" />-->
	</span>
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

	<a href="main.php?p=clanhome"><img src="/images/layout/header_clan.png" border="0" width="179" height="29" onMouseOver="this.src=clan_hover.src" onMouseOut="this.src='/images/layout/header_clan.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=lair&id=95470"><span class="navbar-glow-hover">Dragon Lair</span></a>
	<a class="navbar" href="main.php?p=lair&id=95470&tab=hatchery"><span class="navbar-glow-hover">Nesting Grounds</span></a>

	<span style="position:relative; display:inline-block">
	<a class="navbar" href="main.php?p=gather"><span class="navbar-glow-hover">Gather Items</span></a>




	</span>

	<a class="navbar" href="main.php?p=lair&tab=userpage&id=95470"><span class="navbar-glow-hover">Clan Profile</span></a>
	<a class="navbar" href="main.php?p=hoard"><span class="navbar-glow-hover">Hoard</span></a>
	<a class="navbar" href="main.php?p=bestiary"><span class="navbar-glow-hover">Bestiary</span></a>
	<a class="navbar" href="main.php?p=pm"><span class="navbar-glow-hover">Messages</span></a>

	<a href="main.php?p=shophome"><img src="/images/layout/header_shop.png" border="0" width="179" height="29" onMouseOver="this.src=shop_hover.src" onMouseOut="this.src='/images/layout/header_shop.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=ge"><span class="navbar-glow-hover">Purchase Gems</span></a>
	<a class="navbar" href="main.php?p=market"><span class="navbar-glow-hover">Marketplace</span></a>
	<a class="navbar" href="main.php?p=ah"><span class="navbar-glow-hover">Auction House</span></a>
	<a class="navbar" href="main.php?p=tradepost"><span class="navbar-glow-hover">Trading Post</span></a>
	<a class="navbar" href="main.php?p=crossroads"><span class="navbar-glow-hover">Crossroads</span></a>
	<a class="navbar" href="main.php?p=skins"><span class="navbar-glow-hover">Custom Skins</span></a>		<a class="navbar" href="main.php?p=festive"><span class="navbar-glow-hover">Festive Favors</span></a>

	<a href="main.php?p=playhome"><img src="/images/layout/header_play.png" border="0" width="179" height="29" onMouseOver="this.src=play_hover.src" onMouseOut="this.src='/images/layout/header_play.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=faire"><span class="navbar-glow-hover">Fairgrounds</span></a>
	<a class="navbar" href="main.php?p=coliseum"><span class="navbar-glow-hover">Coliseum</span></a>
		<a class="navbar" href="main.php?p=dominance"><span class="navbar-glow-hover">Dominance</span></a>
	<!--<a class="navbar" href="#">Adventure</a>-->

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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456205108' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456205108' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456205108&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
<img src="/images/layout/arcane/internal_bg.jpg" style="position:absolute; right:0px;" />
<div style="position:relative; width:730px; margin:10px;" id="super-container">
	<script type="text/javascript">
	function ValidateLair(form)
	{
		var valid = 0;

		if (form.dragon.checked == false) {
		valid++;
		alert ('Please check "Accept" to verify that you want to do this.');
		return false;
		}

		if (valid < 1) {
			form.submit();
		}
	}
	</script>

	<a title="Click here to learn more about this page." class="cluehelp"><img src="/images/layout/icon_help.png" style="position:absolute; right:0px; top:0px; z-index:10px; cursor:pointer;" onclick="helpMe('dragon')" /></a>

		<div style="font-size:12px; color:#000;">
				<a href="main.php?p=lair&id=95470" style="color:#000;">Dragon Lair</a> &raquo;
			<a href="main.php?p=lair&tab=dragon&id=95470&did=6930511" style=" color:#731d08; font-weight:bold;">
			Gemstone			</a>
				</div>



	<div style="position:relative; text-align:right; width:705px; height:69px;">

			<a href="main.php?p=lair&id=95470&did=6930511"><img border="0" src="/images/layout/button_back.png" style="position:absolute; top:25px; left:15px; border: 0px;"></a>

	<span style="font-size:22px; text-align:left; color:#731d08; font-weight:bold; position:absolute; top:20px; left:52px;">
	Gemstone        <br>
        <div style="width:390px; font-size:12px; color:#999; font-weight:normal;">
        	#6930511        </div>
        	</span>



				<span style="position:absolute; bottom:10px; right:110px;">
			<a class="loginbar" style="font-size:11px;" title="This dragon cannot be auctioned. It is wearing apparel or skins, has a familiar, is currently caretaking a nest, is one of your progenitors, or is already listed for sale."><img src="/images/layout/button_auction.png" border="0" /></a>
			</span>

			<span style="position:absolute; bottom:10px; right:-10px;">
			<a class="loginbar" style="font-size:11px;" title="This dragon is ineligible for exaltation. It is wearing apparel or skins, has a familiar, is currently caretaking a nest or is listed for sale."><img src="/images/layout/button_dragonpage_exile.png" border="0" /></a>
			</span>

</span>
	</div>


		<script type="text/javascript">

		$(function(){


			$('#close').click(function(e){
				$('#exile').dialog('close');
			});


			$('#exdrag').click(function(e){

				$('#exile').dialog({
					autoOpen: false,
					width: 375,
					height: 'auto',
					title: "Exalt Dragon",
					modal: true,
					resizable: false,
					draggable: false,
					closeOnEscape: false,
					open: function(event, ui) {
						$(".ui-dialog-titlebar-close", ui.dialog).hide();
					}
				});

				$('#exile').dialog('open');

        	});

			$('form#exileform').submit(function(e){

				data = $(this).serialize();
				$.post('includes/ol/exiledragon.php', data)
				.done(function( msg ) {

					$('#exiled').dialog({
						autoOpen: false,
						width: 375,
						height: 'auto',
						title: 'Exalt Dragon',
						modal: true,
						resizable: false,
						draggable: false,
						closeOnEscape: false,
   						open: function(event, ui) {
							$(".ui-dialog-titlebar-close", ui.dialog).hide();
						}
					});

					$("#exiled").html(msg);
					$('#exile').dialog('close');
					$('#exiled').dialog('open');

				});

				return false;

			});




		});
		</script>
			<div id="exiled" style="display:none;"></div>

			<div id="exile" style="display:none;">
									<div style="width:325px; margin-left:auto; margin-right:auto; text-align:center; margin-bottom:10px; margin-top:10px; padding:10px; font-size:12px;">
					<span style="margin-bottom:40px; display:inline-block;">This dragon is a caretaker of your clan's nests and is ineligible for exaltation right now.</span>
					<input type="button" value="Go Back" id="close" class="beigebutton thingbutton">

					</div>
								</div>

				<div style="width:700px; margin-left:auto; margin-right:auto; position:relative;">

			<div id="dragbuttons">
			        		<img src="/rendern/350/69306/6930511_350.png?mtime=VTWbIwACAqc" width="350" height="350" />
        		<a style="border: 0px;" href="main.php?p=lair&tab=dragon&id=95470&did=21327465"><img id="buttonprev" src="/images/layout/button_drag_prev.png" border="0" /></a>
				<a style="border: 0px;" href="main.php?p=lair&tab=dragon&id=95470&did=6930512"><img id="buttonnext" src="/images/layout/button_drag_next.png" border="0" /></a>
							</div>


		<div id="newname" style="position:absolute; right:10px; top:0px; width:320px; height:390px; margin-bottom:10px;">
			<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; width:320px;">
				<!--<legend style="margin-left:5px; font-weight:bold; font-size:13px; width:100px; text-align:left; background-color:#731d08; color:#e8cc9f; padding:5px; border:solid 1px #000; -moz-border-radius:.75em; -khtml-border-radius:.75em; -webkit-border-radius:.75em; border-radius:.75em;"><span style="width:100px; display:inline-block; text-align:center;">Details</span></legend>-->

					<div style="text-align:right; width:300px; margin-right:auto; margin-left:auto;">
											<a class="loginbar" TITLE="This dragon will not be available to breed for 15 days."><img src="/images/icons/breeding_cooldown.png"  /></a>
												<a class="loginbar" TITLE="This dragon is currently enjoying the company of a familiar."><img src="/images/icons/famicon.png"  /></a>

					<a class="elemclue" TITLE="Arcane Dragon"><img src="/images/icons/arcane_rune_20.png" /></a>
					<a class="miniclue" TITLE="Female Dragon"><img src="/images/icons/small_female.png" /></a>
					</div>

					<div style="width:310px; margin-left:auto; margin-right:auto;">

					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Info
					</span>

					<span style="display:inline-block; width:240px; border:1px solid #aaa79e; background-color:#F5F5F5;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">
						<div style="font-weight:bold;">Level 20</div>
						<div style="margin-left:20px;">Fae Female</div>

						<div style="font-weight:bold;">Hatchday</div>
						<div style="margin-left:20px;">Oct 13, 2014 (1 year)</div>
					</div>
					</span>


					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Stats
					</span>

					<span style="display:inline-block; width:240px; border:1px solid #aaa79e; border-top:none; background-color:#EEE;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">

						<a class="cluestat" rel="includes/ol/dstats.php?d=6930511&s=str" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">STR</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<span style="display:inline-block; width:60px;"></span>

						<a class="cluestat" rel="includes/ol/dstats.php?d=6930511&s=int" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">INT</span><span style="display:inline-block; width: 30px; text-align: right;color: #00CC00;">90</span>
						</a>

						<br>

						<a class="cluestat" rel="includes/ol/dstats.php?d=6930511&s=agi" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">AGI</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<span style="display:inline-block; width:60px;"></span>

						<a class="cluestat" rel="includes/ol/dstats.php?d=6930511&s=vit" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">VIT</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<br>

						<a class="cluestat" rel="includes/ol/dstats.php?d=6930511&s=def" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">DEF</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<span style="display:inline-block; width:60px;"></span>

						<a class="cluestat" rel="includes/ol/dstats.php?d=6930511&s=mnd" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">MND</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<br>

						<a class="cluestat" rel="includes/ol/dstats.php?d=6930511&s=qck" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">QCK</span>
						<span style="display:inline-block; width: 30px; text-align: right;">44</span>
						</a>

					</div>
					</span>

					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Growth
					</span>
										<span style="display:inline-block; width:240px; border:1px solid #aaa79e; border-top:none; background-color:#f5f5f5;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">
						<span style="width:55px; display:inline-block;">
							<div style="font-weight:bold;">Length</div>
							0.58M
						</span>

						<span style="margin-left:10px; width:55px; display:inline-block;">
							<div style="font-weight:bold;">Wingspan</div>
							1.07M
						</span>

						<span style="margin-left:10px; width:70px; display:inline-block;">
							<div style="font-weight:bold;">Weight</div>
							3.09KG
						</span>
					</div>
					</span>

					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Genes
					</span>

					<span style="display:inline-block; width:240px; border:1px solid #aaa79e; border-top:none; background-color:#EEE;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">
						<div style="width:200px;"><span style="font-weight:bold; display:inline-block; width:65px;">Primary</span>Purple Basic</div>
						<div style="width:200px;"><span style="font-weight:bold; display:inline-block; width:65px;">Secondary</span>Storm Basic</div>
						<div style="width:200px;"><span style="font-weight:bold; display:inline-block; width:65px;">Tertiary</span>Azure Basic</div>
					</div>
					</span>

					</div>


                    					<div style="width:300px; margin-top:10px; margin-bottom:10px; margin-left:auto; margin-right:auto; background-image:url(images/bars/large_back.png); height:16px; position:relative;">
                    	<span style="position:absolute; text-shadow: 0 0 0.2em #FFF, 0 0 0.2em #FFF, 0 0 0.2em #FFF; margin-top:2px; text-align:center; font-weight:bold; width:300px; margin-right:auto; margin-left:auto; z-index:2;">Energy: 50 / 50</span>
    					<div style="width:300px; overflow:hidden; position:relative; background-image:url(images/bars/large_energy.png); height:16px; z-index:1;"></div>
                    </div>


				<div style="position:relative; width:300px; height:30px; margin-left:auto; margin-right:auto; position:relative; text-align:center;">

						<span style="display:inline; position:absolute; left:35px; top:3px;">
						<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://flightrising.com/main.php?dragon=6930511" data-text="Check out this dragon from Flight Rising! Gemstone!" data-count="none" data-via="FlightRising">Tweet</a>
							<script type="text/javascript" src="//platform.twitter.com/widgets.js"></script>
						</span>

						<span style="display:inline; position:absolute; left:100px; top:2px;">
							<input type="button" value="Generate Code" class="mb_button" onclick="linkDragon('6930511')" />
						</span>

						<script type="text/javascript">
						function linkDragon(id)
						{
							$('body').append('<div id="gencode"></div>');
							$("#gencode").html('<img src="/images/layout/loading.gif"> loading...');

							$('#gencode').dialog({
								autoOpen: false,
								title: "Generate Code",
								width: 400,
								height: "auto",
								modal: true,
								resizable: false,
								draggable: false
							});

							$('#gencode').dialog('open');

							$.ajax({
								type: "POST",
								data: {id: id},
								url: "includes/ol/generate_code.php",
								cache:false
							}).done(function(stuff){
								$("#gencode").html(stuff);
							});
						}
						</script>

						<span style="position:absolute; right:0px;">						<div id="fb-root"></div>
				<script>(function(d, s, id) {
						  var js, fjs = d.getElementsByTagName(s)[0];
						  if (d.getElementById(id)) {return;}
						  js = d.createElement(s); js.id = id;
						  js.src = "//connect.facebook.net/en_US/all.js#appId=175566165856458&xfbml=1";
						  fjs.parentNode.insertBefore(js, fjs);
						}(document, 'script', 'facebook-jssdk'));
				</script>
						<div class="fb-like" data-width="50" data-href="http://flightrising.com/main.php?dragon=6930511" data-send="false" data-layout="button_count" data-width="30" data-show-faces="false" data-action="like" data-font="arial"> </div>						</span>
				</div>
			</fieldset>
		</div>

		<div class="clear" style="height:5px;"></div>

		<div style="float:left; width:230px; margin-right:15px; margin-bottom:10px;">
		<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; height:293px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-top:10px; text-align:center;">Apparel & Skins</div>
			<div style="width:200px; height:200px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:5px; background-color:#EEE; border:solid 1px #BBB; overflow-x:hidden; overflow-y:scroll;">
							<a rel="includes/itemajax.php?id=2980&tab=equipment" class="clue"><img src="/images/cms/equipment/2980.png" width="42" height="42" onclick="appPrev(2980)" style="cursor:pointer;" /></a>
								<a rel="includes/itemajax.php?id=5688&tab=equipment" class="clue"><img src="/images/cms/equipment/5688.png" width="42" height="42" onclick="appPrev(5688)" style="cursor:pointer;" /></a>
								<a rel="includes/itemajax.php?id=2983&tab=equipment" class="clue"><img src="/images/cms/equipment/2983.png" width="42" height="42" onclick="appPrev(2983)" style="cursor:pointer;" /></a>
							</div>
			<div style="text-align:center;">
								<a class="loginbar" title="Click this button to equip custom skins or accents to your dragon." href="http://flightrising.com/main.php?p=lair&id=95470&tab=skins&did=6930511" /><img border="0" src="http://flightrising.com/images/layout/button_skins.png"></a>

					<a class="loginbar" title="Click this button to equip apparel to your dragon." href="http://flightrising.com/main.php?p=lair&id=95470&tab=equip&did=6930511" /><img border="0" src="http://flightrising.com/images/layout/button_apparel.png"></a>
								</div>
		</fieldset>
		<script type="text/javascript">

		function appPrev(itemid){
			$('body').append('<div id="itemprev"></div>');
			$("#itemprev").html('<img src="/images/layout/loading.gif"> loading...');

			$('#itemprev').dialog({
				autoOpen: false,
				title: "Preview Apparel",
				width: 320,
				height: "auto",
				modal: true,
				resizable: false,
				draggable: false,
				closeOnEscape: false,
				position: ["center", 100],
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
				}
			});

			$('#itemprev').dialog('open');

			$.ajax({
				type: "POST",
				data: {itemid: itemid},
				url: "includes/ol/item_preview.php",
				cache:false
			}).done(function(stuff){
				$("#itemprev").html(stuff);
			});
		}

		function skinPrev(itemid)
		{
			$('body').append('<div id="skinprev"></div>');
			$("#skinprev").html('<img src="/images/layout/loading.gif"> loading...');

			$('#skinprev').dialog({
				autoOpen: false,
				title: "Preview Skin #"+itemid,
				width: 470,
				height: "auto",
				modal: true,
				resizable: false,
				draggable: false,
				closeOnEscape: false,
				position: ["center", 100],
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
				}
			});

			$('#skinprev').dialog('open');

			$.ajax({
				type: "POST",
				data: {id: itemid, page: "1"},
				url: "includes/ol/skinprev.php",
				cache:false
			}).done(function(stuff){
				$("#skinprev").html(stuff);
			});
		}
		</script>
		</div>

		<div style="float:left; width:210px; margin-right:15px; margin-bottom:10px;">
		<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; height:293px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-top:10px; text-align:center;">Lineage</div>

			<div style="width:180px; height:200px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:5px; background-color:#EEE; border:solid 1px #BBB; overflow:auto;">

			<div style="color:#76240f; font-size:12px; font-weight:bold; margin-left:10px; margin-top:10px;">Parents</div>
			<div style="margin-left:25px;">
			<em>none</em>			</div>

			<div style="width:160px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:10px;"><img src="/images/layout/graydot.gif" width="160" height="1" /></div>

			<div style="color:#76240f; font-size:12px; font-weight:bold; margin-left:10px; margin-top:10px;">Offspring</div>
			<div style="margin-left:25px;">
			<a href="main.php?p=view&id=60871&tab=dragon&did=7063496" style="color:#000; font-weight:bold; text-decoration:underline;">Nolman</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=7063497" style="color:#000; font-weight:bold; text-decoration:underline;">Azuremantle</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=7475573" style="color:#000; font-weight:bold; text-decoration:underline;">Ester</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=7475574" style="color:#000; font-weight:bold; text-decoration:underline;">Unnamed</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=7475575" style="color:#000; font-weight:bold; text-decoration:underline;">Unnamed</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=9838696" style="color:#000; font-weight:bold; text-decoration:underline;">Una</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=9838697" style="color:#000; font-weight:bold; text-decoration:underline;">Lisil</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=9838698" style="color:#000; font-weight:bold; text-decoration:underline;">Ginessa</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=11473730" style="color:#000; font-weight:bold; text-decoration:underline;">Nicodemus</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=11473731" style="color:#000; font-weight:bold; text-decoration:underline;">Bellurdan</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=14512696" style="color:#000; font-weight:bold; text-decoration:underline;">Pazuzukin</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=14512697" style="color:#000; font-weight:bold; text-decoration:underline;">Gabriel</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=17074122" style="color:#000; font-weight:bold; text-decoration:underline;">Skullcrusher</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=17074123" style="color:#000; font-weight:bold; text-decoration:underline;">Bryan</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=17687793" style="color:#000; font-weight:bold; text-decoration:underline;">Wynne</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=17687794" style="color:#000; font-weight:bold; text-decoration:underline;">Sorrowrunner</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=18273745" style="color:#000; font-weight:bold; text-decoration:underline;">Glitter</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=18273746" style="color:#000; font-weight:bold; text-decoration:underline;">Shiva</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=18273747" style="color:#000; font-weight:bold; text-decoration:underline;">Nideth</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=18766325" style="color:#000; font-weight:bold; text-decoration:underline;">Bold</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=18766326" style="color:#000; font-weight:bold; text-decoration:underline;">Chamomile</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=18766327" style="color:#000; font-weight:bold; text-decoration:underline;">Raccoon</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=18766328" style="color:#000; font-weight:bold; text-decoration:underline;">Kadere</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=19174237" style="color:#000; font-weight:bold; text-decoration:underline;">Prustil</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=19174238" style="color:#000; font-weight:bold; text-decoration:underline;">Ripsaw</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=19174239" style="color:#000; font-weight:bold; text-decoration:underline;">BlueFrosting</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=19174240" style="color:#000; font-weight:bold; text-decoration:underline;">Isavar</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=19639603" style="color:#000; font-weight:bold; text-decoration:underline;">Panori</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=19639604" style="color:#000; font-weight:bold; text-decoration:underline;">Nalani</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=19639605" style="color:#000; font-weight:bold; text-decoration:underline;">Leofrick</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=20114347" style="color:#000; font-weight:bold; text-decoration:underline;">Allray</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=20114348" style="color:#000; font-weight:bold; text-decoration:underline;">Rana</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=20114349" style="color:#000; font-weight:bold; text-decoration:underline;">Ankaa</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=20114350" style="color:#000; font-weight:bold; text-decoration:underline;">Acamar</a><br /><a href="main.php?p=view&id=40492&tab=dragon&did=20562622" style="color:#000; font-weight:bold; text-decoration:underline;">Ankaa</a><br /><a href="main.php?p=view&id=0&tab=dragon&did=20562623" style="color:#000; font-weight:bold; text-decoration:underline;">Adhafera</a><br /><a href="main.php?p=lair&id=95470&tab=dragon&did=21304374" style="color:#000; font-weight:bold; text-decoration:underline;">Unnamed</a><br /><a href="main.php?p=lair&id=95470&tab=dragon&did=21304375" style="color:#000; font-weight:bold; text-decoration:underline;">Unnamed</a><br /><a href="main.php?p=lair&id=95470&tab=dragon&did=21304376" style="color:#000; font-weight:bold; text-decoration:underline;">Unnamed</a><br />			</div>


            <div style="width:160px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:10px;"><img src="/images/layout/graydot.gif" width="160" height="1" /></div>

			<span id="exalts">
			            </span>




            </div>
			<div style="text-align:center;">
            				<a class="loginbar" title="This dragon is currently caretaking a nest and cannot be bred."><img border="0" src="http://flightrising.com/images/layout/breed_inactive.png"></a>
								<a class="loginbar" TITLE="This dragon will not be available to breed for 15 days."><img border="0" src="/images/icons/breeding_cooldown.png"  /></a>
				            </div>
		</fieldset>
		</div>

		<div style="float:left; width:230px; margin-bottom:10px;;">
		<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; height:293px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-top:10px; text-align:center;">Familiar</div>

			<div style="width:205px; height:205px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:5px; background-color:#EEE; border:solid 1px #BBB; overflow:auto;">
							<a rel="includes/itemajax.php?id=7427&tab=familiar" class="clueitem"><img src="/images/cms/familiar/art/7427.png" border="0" /></a>
							</div>
			<div style="text-align:center;">
								<span style="display:inline-block; height:34px; width:61px; margin-right:3px; font-size:10px; color:#731d08; vertical-align:middle; font-weight:bold; text-align:left;">
						Awakened													<img src="/images/bars/bar_bond_max.png" width="61" height="17" border="0" />
												</span>

											<a class="loginbar" title="Click here to bond with your familiar. You may do this once a day.">
						<img src="../images/layout/button_bond.png" width="32" height="34" style="vertical-align:middle; margin-right:3px; cursor:pointer;" border="0" onclick="bondJamesbond('7427')" />
						</a>
						<script type="text/javascript">
						function bondJamesbond(id)
						{

							$('body').append('<div id="bonding"></div>');
							$("#bonding").html('<img src="/images/layout/loading.gif"> loading...');

							$('#bonding').dialog({
								autoOpen: false,
								title: "Bond with Familiar",
								width: 450,
								height: "auto",
								modal: true,
								resizable: false,
								draggable: false,
								closeOnEscape: false,
								open: function(event, ui) {
									$(".ui-dialog-titlebar-close", ui.dialog).hide();
								}
							});

							$('#bonding').dialog('open');

							$.ajax({
								type: "POST",
								data: {id: id},
								url: "includes/ol/fam_bonding.php",
								cache:false
							}).done(function(stuff){
								$("#bonding").html(stuff);
							});
						}
						</script>

										<a class="loginbar" title="Click this button to change what familiar is paired with this dragon." href="main.php?p=lair&id=95470&tab=familiar&did=6930511" /><img border="0" src="http://flightrising.com/images/layout/button_change.png" style="vertical-align:middle;"></a>
							</div>
		</fieldset>
		</div>

		<div class="clear" style="width:700px;">
		<a name="bio"><fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; min-height:263px; padding:10px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-bottom:15px; text-align:center;">Information</div>


		<div style="color: #000000; font-size: 12px; width:640px; overflow:auto; min-height:160px; margin-left:auto; margin-right:auto; background-color:#EEE; border:solid 1px #BBB; padding:20px;">

        </div>
					<div style="text-align:center;"><form method="post" action="main.php?p=lair&id=95470&tab=dragon&did=6930511&action=edit#bio"><input type="submit" value="Edit" class="mb_button" onclick="" /></form></div>
				</fieldset></a>
		<br>&nbsp;



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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456205108' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456205108' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456205108&amp;n=a26545c2' border='0' alt='' /></a></iframe>
		<script type='text/javascript' src='http://162.218.115.228/delivery/ag.php'></script>

		</div></div>
<!--End Bottom Banner-->
<div class="copybar">&copy; 2013 Stormlight Workshop. All Rights Reserved<br />
<a href="main.php?p=tos">Terms of Use</a> | <a href="http://flightrising.com/main.php?board=frd&id=749441&p=mb">Rules and Guidelines</a> | <a href="main.php?p=privacy">Privacy Policy</a> | <a href="main.php?p=credits">Credits</a> |  <a href="index.php?p=contact">Contact Us</a> | <a href="http://www.virtualpetlist.com/" target="_blank" alt="Virtual Pet List">Virtual Pets Forum</a></div>
<!--End Copybar-->

<!--End Container-->
</div>

	<script type="text/javascript">
	</script>

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

DRAGON_PAGE_UNNAMED = """

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta property="og:title" content="slaynsoul's dragon Unnamed - Breed, raise, and train dragons on Flight Rising!"/>
	<meta property="og:type" content="website"/>
	<meta property="og:image" content="/rendern/350/213044/21304374_350.png?mtime=Vso90AABkGE"/>
	<meta property="og:url" content="http://flightrising.com/main.php?dragon=21304374"/>
	<meta property="og:site_name" content="Flight Rising"/>
	<meta property="fb:admins" content="548611600" />
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
			sel.text = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=95470#"+id+"']"+quote+"[/quote]";
		}

		else
    	{  // Code for Mozilla Firefox
			var len = textarea.value.length;
	    	var start = textarea.selectionStart;
			var end = textarea.selectionEnd;


			var scrollTop = textarea.scrollTop;
			var scrollLeft = textarea.scrollLeft;


        	var sel = textarea.value.substring(start, end);
			var rep = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=1&id=95470#"+id+"']"+quote+"[/quote]";
        	textarea.value =  textarea.value.substring(0,start) + rep + textarea.value.substring(end,len);

			textarea.scrollTop = scrollTop;
			textarea.scrollLeft = scrollLeft;
		}
	}
</script>


	<script type="text/javascript">
	function randName(dragon,gen)
	{
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
	  if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
		document.getElementById("repname").innerHTML=xmlhttp.responseText;
		}
	  }
	xmlhttp.open("GET","includes/randnames.php?id="+dragon+"&gen="+gen,false);
	xmlhttp.send();
	}
	</script>


</head>





	<body style="background-image: url(/images/layout/arcane/bg.jpg); position:relative;">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/arcane/banner.jpg);">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	21:29    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">2342 Users Online</a></strong>
	</span>

	<!--Food-->
		<span id="food_bar">
	<span style="position:absolute; left:205px; bottom:2px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat insects.">
	<img src="/images/layout/icon_insect.png" width="26" height="20" border="0" align="absmiddle">
	291	</a>
	</span>

	<span style="position:absolute; left:305px; bottom:4px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat meat.">
	<img src="/images/layout/icon_meat.png" width="27" height="16" border="0" align="absmiddle">
	404	</a>
	</span>

	<span style="position:absolute; left:405px; bottom:3px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat seafood.">
	<img src="/images/layout/icon_seafood.png" width="24" height="18" border="0" align="absmiddle">
	340	</a>
	</span>

	<span style="position:absolute; left:505px; bottom:2px; text-align:left; cursor:default;">
	<a class="loginlinks loginbar" style="font-size:11px;" title="This is how much food you have for dragons that eat plants.">
	<img src="/images/layout/icon_plant.png" width="25" height="19" border="0" align="absmiddle">
	411	</a>
	</span>
	</span>
		<!--End Food-->



	<div style="position:absolute; bottom:2px; right:130px; cursor:pointer; height:20px;">
		<a id="messcnt" class="loginlinks loginbar" title="This shows how many new messages you have. Clicking this icon will take you directly to your inbox, where you can send and receive messages with other users." style="font-size:11px; cursor:pointer;" href="main.php?p=pm">
		<img id="messimg" src="../images/layout/small_message.png" width="30" height="20" align="absmiddle" border="0" />
		<span id="messalert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<div style="position:absolute; bottom:2px; right:70px; cursor:pointer; height:20px;">
		<a id="frensm" class="loginlinks loginbar" title="Click this icon to access your pending friend requests or view your friends list. You may accept or reject requests from this menu." style="font-size:11px; cursor:pointer;">
		<img id="frensimg" src="../images/layout/friends_icon.png" width="20" height="20" align="abstop" border="0" />
		<span id="frensalert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:absolute; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<div style="position:absolute; bottom:2px; right:10px; cursor:pointer; height:20px;">
		<a id="alertm" class="loginlinks loginbar" title="This lets you know how many new alerts you have. Clicking the Alerts icon will let you know about your recent clan and friend activity." style="font-size:11px; cursor:pointer;">
		<img id="alertimg" src="../images/layout/small_alert.png" width="23" height="20" align="absmiddle" border="0" />
		<span id="alert" style="font-size:11px; display:inline-block; width:21px; height:19px;">
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; ">
				0			</div>
		</span>
		</a>
	</div>








	<script type="text/javascript">
	$(document).mouseup(function (e){
		//var container = $("#alertwin");

		if (!$("#alertwin").is(e.target) && $("#alertwin").has(e.target).length === 0)
		{
			$("#alertwin").dialog('close');
			$('#alertwin').detach();
		}

		//var container2 = $("#logwin");

		if (!$("#logwin").is(e.target) && $("#logwin").has(e.target).length === 0)
		{
			$("#logwin").dialog('close');
			$('#logwin').detach();
		}


		if (!$("#frenswin").is(e.target) && $("#frenswin").has(e.target).length === 0)
		{
			$("#frenswin").dialog('close');
			$('#frenswin').detach();
		}

	});

	$("#alertm").click(function() {

		$('body').append('<div id="alertwin" style="display:none;"></div>');
		$("#alertwin").html('<img src="/images/layout/loading.gif"> loading...');

		$('#alertwin').dialog({
			title: "",
			width: 300,
			minHeight: 25,
			maxHeight: 200,
			modal:false,
			draggable:false,
			resizable:false,
			show: 'blind',
			position: {
				my: 'right top',
				at: 'right bottom',
				of: $('#alertimg')
			},
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
				$(".ui-dialog-titlebar", ui.dialog).hide();
			}
		});

		$('#alertwin').dialog('open');

		var data = '';
		$.ajax({
			type: "POST",
			data: data,
			url: "includes/ol/alerts.php",
			cache:false
		}).done(function(stuff){
			$("#alertwin").html(stuff);


			$.ajax({
				type: "POST",
				data: "",
				url: "includes/ol/alert_count.php",
				cache:false
			}).done(function(stuff){
				$("#alert").html(stuff);
			});


		});

	});

	$("#frensm").click(function() {

		$('body').append('<div id="frenswin" style="display:none;"></div>');
		$("#frenswin").html('<img src="/images/layout/loading.gif"> loading...');

		$('#frenswin').dialog({
			title: "",
			width: 300,
			minHeight: 25,
			maxHeight: 200,
			modal:false,
			draggable:false,
			resizable:false,
			show: 'blind',
			position: {
				my: 'right top',
				at: 'right bottom',
				of: $('#frensimg')
			},
			open: function(event, ui) {
				$(".ui-dialog-titlebar-close", ui.dialog).hide();
				$(".ui-dialog-titlebar", ui.dialog).hide();
			}
		});

		$('#frenswin').dialog('open');

		var data = '';
		$.ajax({
			type: "POST",
			data: data,
			url: "includes/ol/frensreq.php",
			cache:false
		}).done(function(stuff){
			$("#frenswin").html(stuff);
		});

	});

	</script>
	<!--<div id="alertwin" style="display:none;"></div>	-->
	<!--<div id="frenswin" style="display:none;"></div>	-->

</div>

</div>

	<div id="ticker" style="position:absolute; background-image:url(/images/layout/ticker_topbar.png); right:0px; top:0px; height:24px; width:285px; font-size:10px; color:#393939; overflow:hidden;">

			<div class="rotating-item" id="tick1" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/achievement.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=achieve">Earn achievements as your clan grows.</a>
		</div>
				<div class="rotating-item" id="tick2" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/feed.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=gather">Well-fed clans earn daily bonuses.</a>
		</div>
				<div class="rotating-item" id="tick3" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/Bug.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=mb&board=bug">Found a bug? Tell us about it!</a>
		</div>
				<div class="rotating-item" id="tick4" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/heart_big.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=bestiary">Bond with your familiars daily for rewards.</a>
		</div>
				<div class="rotating-item" id="tick5" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/tumblr.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.tumblr.com/">Follow Flight Rising on Tumblr</a>
		</div>
				<div class="rotating-item" id="tick6" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/deviant.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.deviantart.com/">Flight Rising Deviantart: Share Your Art!</a>
		</div>
				<div class="rotating-item" id="tick7" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/tomo.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=tradepost&lot=trivia">Test your trivia skills with Tomo!</a>
		</div>
				<div class="rotating-item" id="tick8" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/status.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/site/status">Keep up to date on the status of FR!</a>
		</div>
				<div class="rotating-item" id="tick9" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/15573.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1704902">Thylacine tertiary gene discovered.</a>
		</div>
				<div class="rotating-item" id="tick10" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/swipp2.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1623317">Meet Pipp and Tripp at the Swap Stand!</a>
		</div>
				<div class="rotating-item" id="tick11" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/15702.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1716128">Sylvan apparel is now stocking.</a>
		</div>
				<div class="rotating-item" id="tick12" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/rainbowscarf2.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://flightrising.com/main.php?p=market&type=1&tab=app">Prismatic Silks are now available.</a>
		</div>
				<div class="rotating-item" id="tick13" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/familiarcontest.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1749772">Familiar coloring contest results are in!</a>
		</div>
				<div class="rotating-item" id="tick14" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/16004.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="http://www1.flightrising.com/forums/ann/1734727">Stained: new tertiary gene now available.</a>
		</div>
				<div class="rotating-item" id="tick15" style="display:none; position:absolute; top:2px; left:15px;">
			<span style="display:inline-block; height:15px; width:15px; margin-right:10px;"><img src="/images/cms/ticker/7.png" height="15" width="15" style="vertical-align:middle;"/></span>
			<a style="color:#393939; text-decoration:none; line-height:15px; vertical-align:middle;" href="main.php?p=dominance">The Shadow flight is dominating!</a>
		</div>

	</div>
	<script type="text/javascript">

	$(window).load(function() { //start after HTML, images have loaded
		var InfiniteRotator =
		{
			init: function()
			{
				//initial fade-in time (in milliseconds)
				var initialFadeIn = 1000;
				//interval between items (in milliseconds)
				var itemInterval = 13000;
				//cross-fade time (in milliseconds)
				var fadeTime = 2500;
				//count number of items
				var numberOfItems = $('.rotating-item').length;
				//set current item
				var currentItem = 0;
				//show first item
				$('.rotating-item').eq(currentItem).fadeIn(initialFadeIn);
				//loop through the items
				var infiniteLoop = setInterval(function(){
					$('.rotating-item').eq(currentItem).fadeOut(fadeTime);

					if(currentItem == numberOfItems -1){
						currentItem = 0;
					}else{
						currentItem++;
					}
					$('.rotating-item').eq(currentItem).fadeIn(fadeTime);

				}, itemInterval);
			}
		};

		InfiniteRotator.init();

	});
	</script>

<div id="usertab" style="position:absolute; background-image:url(/images/layout/user_module_bg.png); right:0px; bottom:31px; height:112px; width:285px;">
	<span style="width:60px; height:60px; display:inline-block; position:absolute; top:10px; left:10px; background-color:#FFF;" id="ltavtr">
		<a href="main.php?p=lair&tab=userpage&id=95470"><img src="/rendern/portraits/71663/7166200p.png?mtime=VN2ddAAANvE" height="60" width="60" style="border:1px solid #000;" /></a>
	</span>

			<span style="width:60px; height:60px; display:inline-block; position:absolute; top:71px; left:10px;">
			<img src="/images/layout/elemental_banners/arcane_banner.png" height="60" width="60" />
		</span>
			<span style="width:185px; height:20px; display:inline-block; position:absolute; top:7px; left:85px; ">
		<a href="main.php?p=lair&tab=userpage&id=95470"><span style="color:#731d08; font-size:15px; font-weight:bold;">slaynsoul</span></a>
		<img src="../images/icons/down_arrow.png" width="15" height="15" id="logbutton" style="vertical-align:text-bottom; cursor:pointer;" />

		<script type="text/javascript">

		$("#logbutton").click(function() {
			$('body').append('<div id="logwin" style="display:none;"></div>');
			$("#logwin").html('<img src="/images/layout/loading.gif"> loading...');

			$('#logwin').dialog({
				title: "",
				width: 135,
				minHeight: 25,
				maxHeight: 200,
				modal:false,
				draggable:false,
				resizable:false,
				show: 'blind',
				position: {
					my: 'left top',
					at: 'left top',
					of: $('#logbutton')
				},
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
					$(".ui-dialog-titlebar", ui.dialog).hide();
				}
			});

			$('#logwin').dialog('open');

			$.ajax({
				type: "POST",
				data: '',
				url: "includes/ol/user_window.php",
				cache:false
			}).done(function(stuff){
				$("#logwin").html(stuff);
			});

		});



		</script>


	</span>



	<span style="text-align:left; cursor:default; position:absolute; left:210px; bottom:3px;">
		<a class="loginlinks loginbar" title="Achievements are earned by completing specific and sometimes difficult tasks." style="color:#731d08;" href="main.php?p=achieve">
		<span id="login_ach" style="position:relative; height:25px; width:25px; display:inline-block;">
			<img src="/images/layout/icon_achievements.png" width="25" height="25" border="0" align="absmiddle" style="position:absolute; right:0px; bottom:0px; z-index:20;" id="overlay_ach">
			<img src="/images/layout/icon_achievements.png" width="25" height="25" border="0" align="absmiddle">
		</span>

		<span style="font-size:11px;">
		1095		</span>
		</a>
	</span>



	<span style="position:absolute; left:210px; top:57px; text-align:left;" id="bstcount">

	<a class="loginlinks loginbar" style="color:#731d08; font-size:11px;" title="This shows how many familiars your clan has befriended. This number increases with each unique new familiar you have in your hoard or accompanying your dragons. Clicking this icon will take you directly to your Bestiary." href="main.php?p=bestiary">
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 359	</a>

	</span>



	<span style="position:absolute; left:85px; display:inline-block; top:28px; width:185px; height:26px;">
    <a rel="includes/ol/nrg_tooltip.php?percent=100&wellfed=3" class="clue_nrg">

    <div style="position:absolute; top:0px; left:0px; width:185px; background-image:url(images/bars/avg_back.png); height:20px;">
    	<span style="position:absolute; text-shadow: 0 0 0.2em #FFF, 0 0 0.2em #FFF, 0 0 0.2em #FFF; margin-top:2px; text-align:center; font-weight:bold; width:180px; margin-right:auto; margin-left:auto; z-index:2;">100%</span>
    	<div style="width:185px; overflow:hidden; position:relative; background-image:url(images/bars/avg_energy.png); height:20px;">
		</div>
    </div>

    <img style="position:absolute; top:20px; left:0px;" border="0" src="/images/bars/day3bar.png" width="185" height="6" />

    </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; top:60px;" >
		<a class="loginbar loginlinks" title="This is how much treasure you have collected in your lair." onclick="window.location='main.php?p=hoard'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_treasure.png" border="0" align="absmiddle">

                	<span id="user_treasure" style="font-size:11px;">1378362</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3068</span>
		</a>
		<!--<input style="width:40px; height:20px; font-size:10px; font-weight:bold; color:#000; background-color:#f4f4f4; border:solid 1px #000; -moz-border-radius:0.4em; -khtml-border-radius:0.4em; -webkit-border-radius:0.4em; border-radius:0.4em;" type="button" name="refill" value="Add" onclick="window.location='main.php?p=ge'" />-->
	</span>
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

	<a href="main.php?p=clanhome"><img src="/images/layout/header_clan.png" border="0" width="179" height="29" onMouseOver="this.src=clan_hover.src" onMouseOut="this.src='/images/layout/header_clan.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=lair&id=95470"><span class="navbar-glow-hover">Dragon Lair</span></a>
	<a class="navbar" href="main.php?p=lair&id=95470&tab=hatchery"><span class="navbar-glow-hover">Nesting Grounds</span></a>

	<span style="position:relative; display:inline-block">
	<a class="navbar" href="main.php?p=gather"><span class="navbar-glow-hover">Gather Items</span></a>




	</span>

	<a class="navbar" href="main.php?p=lair&tab=userpage&id=95470"><span class="navbar-glow-hover">Clan Profile</span></a>
	<a class="navbar" href="main.php?p=hoard"><span class="navbar-glow-hover">Hoard</span></a>
	<a class="navbar" href="main.php?p=bestiary"><span class="navbar-glow-hover">Bestiary</span></a>
	<a class="navbar" href="main.php?p=pm"><span class="navbar-glow-hover">Messages</span></a>

	<a href="main.php?p=shophome"><img src="/images/layout/header_shop.png" border="0" width="179" height="29" onMouseOver="this.src=shop_hover.src" onMouseOut="this.src='/images/layout/header_shop.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=ge"><span class="navbar-glow-hover">Purchase Gems</span></a>
	<a class="navbar" href="main.php?p=market"><span class="navbar-glow-hover">Marketplace</span></a>
	<a class="navbar" href="main.php?p=ah"><span class="navbar-glow-hover">Auction House</span></a>
	<a class="navbar" href="main.php?p=tradepost"><span class="navbar-glow-hover">Trading Post</span></a>
	<a class="navbar" href="main.php?p=crossroads"><span class="navbar-glow-hover">Crossroads</span></a>
	<a class="navbar" href="main.php?p=skins"><span class="navbar-glow-hover">Custom Skins</span></a>		<a class="navbar" href="main.php?p=festive"><span class="navbar-glow-hover">Festive Favors</span></a>

	<a href="main.php?p=playhome"><img src="/images/layout/header_play.png" border="0" width="179" height="29" onMouseOver="this.src=play_hover.src" onMouseOut="this.src='/images/layout/header_play.png'" style="margin-top:10px; margin-bottom:5px;" /></a>
	<a class="navbar" href="main.php?p=faire"><span class="navbar-glow-hover">Fairgrounds</span></a>
	<a class="navbar" href="main.php?p=coliseum"><span class="navbar-glow-hover">Coliseum</span></a>
		<a class="navbar" href="main.php?p=dominance"><span class="navbar-glow-hover">Dominance</span></a>
	<!--<a class="navbar" href="#">Adventure</a>-->

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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456205365' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456205365' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456205365&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
<img src="/images/layout/arcane/internal_bg.jpg" style="position:absolute; right:0px;" />
<div style="position:relative; width:730px; margin:10px;" id="super-container">
	<script type="text/javascript">
	function ValidateLair(form)
	{
		var valid = 0;

		if (form.dragon.checked == false) {
		valid++;
		alert ('Please check "Accept" to verify that you want to do this.');
		return false;
		}

		if (valid < 1) {
			form.submit();
		}
	}
	</script>

	<a title="Click here to learn more about this page." class="cluehelp"><img src="/images/layout/icon_help.png" style="position:absolute; right:0px; top:0px; z-index:10px; cursor:pointer;" onclick="helpMe('dragon')" /></a>

		<div style="font-size:12px; color:#000;">
				<a href="main.php?p=lair&id=95470" style="color:#000;">Dragon Lair</a> &raquo;
			<a href="main.php?p=lair&tab=dragon&id=95470&did=21304374" style=" color:#731d08; font-weight:bold;">
			Unnamed			</a>
				</div>



	<div style="position:relative; text-align:right; width:705px; height:69px;">

			<a href="main.php?p=lair&id=95470&did=21304374"><img border="0" src="/images/layout/button_back.png" style="position:absolute; top:25px; left:15px; border: 0px;"></a>

	<span style="font-size:22px; text-align:left; color:#731d08; font-weight:bold; position:absolute; top:20px; left:52px;">
				<script type="text/javascript">
			function babyName(id, str)
			{
				$.ajax({
					type: "POST",
					data: {id: id, name: str},
					url: "includes/ol/babynames.php",
					cache:false
				}).done(function(stuff){
					$("#naming").html(stuff);

					$('#naming').dialog({
						autoOpen: false,
						title: "Name Dragon",
						width: 375,
						height: 180,
						modal: true,
						resizable: false,
						draggable: false//,
//						closeOnEscape: false//,
//						open: function(event, ui) {
//							$(".ui-dialog-titlebar-close", ui.dialog).hide();
//						}
					});

					$('#naming').dialog('open');

				});
			}
			</script>
			<div id="naming"></div>
			Unnamed <img src="/images/layout/button_rename.png" style="vertical-align:middle; cursor:pointer;" border="0" onclick="babyName(' 21304374', '')" />
			<!--<input type="button" value="Name Dragon" class="mb_button" style="font-size:16px; font-weight:bold; padding:5px; cursor:pointer; color:#fff; background-color:#731d08;" onclick="babyName('21304374', '');" /> -->
			        <br>
        <div style="width:390px; font-size:12px; color:#999; font-weight:normal;">
        	#21304374        </div>
        	</span>



					<span style="position:absolute; bottom:10px; right:110px;">
				<a class="loginbar" style="font-size:11px; cursor:pointer;" id="selldrag" title="Place this dragon on the auction house, where other users can purchase it." href="main.php?p=ah&action=sell&tab=dragons&id=21304374"><img src="/images/layout/button_auction.png" border="0" /></a>
				</span>

				<span style="position:absolute; bottom:10px; right:-10px;">
				<a class="loginbar" style="font-size:11px; cursor:pointer;" id="exdrag" title="Send this dragon to directly serve under your flight's elemental god. Such a high honor will remove them from your lair forever. They will leave behind their own personal stash of riches."><img src="/images/layout/button_dragonpage_exile.png" border="0" /></a>
				</span>

</span>
	</div>


		<script type="text/javascript">

		$(function(){


			$('#close').click(function(e){
				$('#exile').dialog('close');
			});


			$('#exdrag').click(function(e){

				$('#exile').dialog({
					autoOpen: false,
					width: 375,
					height: 'auto',
					title: "Exalt Dragon",
					modal: true,
					resizable: false,
					draggable: false,
					closeOnEscape: false,
					open: function(event, ui) {
						$(".ui-dialog-titlebar-close", ui.dialog).hide();
					}
				});

				$('#exile').dialog('open');

        	});

			$('form#exileform').submit(function(e){

				data = $(this).serialize();
				$.post('includes/ol/exiledragon.php', data)
				.done(function( msg ) {

					$('#exiled').dialog({
						autoOpen: false,
						width: 375,
						height: 'auto',
						title: 'Exalt Dragon',
						modal: true,
						resizable: false,
						draggable: false,
						closeOnEscape: false,
   						open: function(event, ui) {
							$(".ui-dialog-titlebar-close", ui.dialog).hide();
						}
					});

					$("#exiled").html(msg);
					$('#exile').dialog('close');
					$('#exiled').dialog('open');

				});

				return false;

			});




		});
		</script>
			<div id="exiled" style="display:none;"></div>

			<div id="exile" style="display:none;">
									<div style="width:295px; margin-left:15px; margin-right:15px; margin-top:15px; text-align:center; margin-bottom:10px; margin-top:10px; padding:10px; font-size:12px;">
					Exalting <span style="font-weight:bold;">Unnamed</span> to the service of the <span style="font-weight:bold;">Arcanist</span> will remove them from your lair forever. They will leave behind a small sum of riches that they have accumulated. This action is irreversible.<br />
					<br />
					Do you wish to continue?
					<form method="post" style="margin-top:25px;" name="exileform" id="exileform">
					<input type="hidden" name="dragon" id="dragon" value="21304374" />
					<input type="submit" value="Exalt Dragon" class="beigebutton thingbutton">
					<input type="button" value="Cancel" id="close" class="redbutton anybutton">
					</form>
					</div>
								</div>

				<div style="width:700px; margin-left:auto; margin-right:auto; position:relative;">

			<div id="dragbuttons">
			        		<img src="/rendern/350/213044/21304374_350.png?mtime=Vso90AABkGE" width="350" height="350" />
        		<a style="border: 0px;" href="main.php?p=lair&tab=dragon&id=95470&did=19959492"><img id="buttonprev" src="/images/layout/button_drag_prev.png" border="0" /></a>
				<a style="border: 0px;" href="main.php?p=lair&tab=dragon&id=95470&did=21304375"><img id="buttonnext" src="/images/layout/button_drag_next.png" border="0" /></a>
							</div>


		<div id="newname" style="position:absolute; right:10px; top:0px; width:320px; height:390px; margin-bottom:10px;">
			<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; width:320px;">
				<!--<legend style="margin-left:5px; font-weight:bold; font-size:13px; width:100px; text-align:left; background-color:#731d08; color:#e8cc9f; padding:5px; border:solid 1px #000; -moz-border-radius:.75em; -khtml-border-radius:.75em; -webkit-border-radius:.75em; border-radius:.75em;"><span style="width:100px; display:inline-block; text-align:center;">Details</span></legend>-->

					<div style="text-align:right; width:300px; margin-right:auto; margin-left:auto;">
											<a class="loginbar" TITLE="This dragon will not be available to breed for 14 days."><img src="/images/icons/breeding_cooldown.png"  /></a>

					<a class="elemclue" TITLE="Arcane Dragon"><img src="/images/icons/arcane_rune_20.png" /></a>
					<a class="miniclue" TITLE="Male Dragon"><img src="/images/icons/small_male.png" /></a>
					</div>

					<div style="width:310px; margin-left:auto; margin-right:auto;">

					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Info
					</span>

					<span style="display:inline-block; width:240px; border:1px solid #aaa79e; background-color:#F5F5F5;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">
						<div style="font-weight:bold;">Level 1</div>
						<div style="margin-left:20px;">Fae Male</div>

						<div style="font-weight:bold;">Hatchday</div>
						<div style="margin-left:20px;">Feb 21, 2016 (1 day)</div>
					</div>
					</span>


					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Stats
					</span>

					<span style="display:inline-block; width:240px; border:1px solid #aaa79e; border-top:none; background-color:#EEE;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">

						<a class="cluestat" rel="includes/ol/dstats.php?d=21304374&s=str" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">STR</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<span style="display:inline-block; width:60px;"></span>

						<a class="cluestat" rel="includes/ol/dstats.php?d=21304374&s=int" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">INT</span><span style="display:inline-block; width: 30px; text-align: right;">8</span>
						</a>

						<br>

						<a class="cluestat" rel="includes/ol/dstats.php?d=21304374&s=agi" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">AGI</span>
						<span style="display:inline-block; width: 30px; text-align: right;">8</span>
						</a>

						<span style="display:inline-block; width:60px;"></span>

						<a class="cluestat" rel="includes/ol/dstats.php?d=21304374&s=vit" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">VIT</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<br>

						<a class="cluestat" rel="includes/ol/dstats.php?d=21304374&s=def" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">DEF</span>
						<span style="display:inline-block; width: 30px; text-align: right;">5</span>
						</a>

						<span style="display:inline-block; width:60px;"></span>

						<a class="cluestat" rel="includes/ol/dstats.php?d=21304374&s=mnd" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">MND</span>
						<span style="display:inline-block; width: 30px; text-align: right;">8</span>
						</a>

						<br>

						<a class="cluestat" rel="includes/ol/dstats.php?d=21304374&s=qck" style="margin:0px; padding:0px; color:#000;">
						<span style="display:inline-block; width:30px; font-weight:bold;">QCK</span>
						<span style="display:inline-block; width: 30px; text-align: right;">6</span>
						</a>

					</div>
					</span>

					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Growth
					</span>
										<span style="display:inline-block; width:240px; border:1px solid #aaa79e; border-top:none; background-color:#f5f5f5;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">
						<span style="width:55px; display:inline-block;">
							<div style="font-weight:bold;">Length</div>
							0.21M
						</span>

						<span style="margin-left:10px; width:55px; display:inline-block;">
							<div style="font-weight:bold;">Wingspan</div>
							0.16M
						</span>

						<span style="margin-left:10px; width:70px; display:inline-block;">
							<div style="font-weight:bold;">Weight</div>
							0.41KG
						</span>
					</div>
					</span>

					<span style="text-align:right; vertical-align:top; width:50px; margin-right:10px; font-size:12px; font-weight:bold; color:#731d08; display:inline-block;">
						Genes
					</span>

					<span style="display:inline-block; width:240px; border:1px solid #aaa79e; border-top:none; background-color:#EEE;">
					<div style="margin-left:10px; margin-bottom:5px; margin-top:5px;">
						<div style="width:200px;"><span style="font-weight:bold; display:inline-block; width:65px;">Primary</span>Caribbean Basic</div>
						<div style="width:200px;"><span style="font-weight:bold; display:inline-block; width:65px;">Secondary</span>Lavender Basic</div>
						<div style="width:200px;"><span style="font-weight:bold; display:inline-block; width:65px;">Tertiary</span>Orange Basic</div>
					</div>
					</span>

					</div>


                    					<div style="width:300px; margin-top:10px; margin-bottom:10px; margin-left:auto; margin-right:auto; background-image:url(images/bars/large_back.png); height:16px; position:relative;">
                    	<span style="position:absolute; text-shadow: 0 0 0.2em #FFF, 0 0 0.2em #FFF, 0 0 0.2em #FFF; margin-top:2px; text-align:center; font-weight:bold; width:300px; margin-right:auto; margin-left:auto; z-index:2;">Energy: 50 / 50</span>
    					<div style="width:300px; overflow:hidden; position:relative; background-image:url(images/bars/large_energy.png); height:16px; z-index:1;"></div>
                    </div>


				<div style="position:relative; width:300px; height:30px; margin-left:auto; margin-right:auto; position:relative; text-align:center;">

						<span style="display:inline; position:absolute; left:35px; top:3px;">
						<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://flightrising.com/main.php?dragon=21304374" data-text="Check out this dragon from Flight Rising! Unnamed!" data-count="none" data-via="FlightRising">Tweet</a>
							<script type="text/javascript" src="//platform.twitter.com/widgets.js"></script>
						</span>

						<span style="display:inline; position:absolute; left:100px; top:2px;">
							<input type="button" value="Generate Code" class="mb_button" onclick="linkDragon('21304374')" />
						</span>

						<script type="text/javascript">
						function linkDragon(id)
						{
							$('body').append('<div id="gencode"></div>');
							$("#gencode").html('<img src="/images/layout/loading.gif"> loading...');

							$('#gencode').dialog({
								autoOpen: false,
								title: "Generate Code",
								width: 400,
								height: "auto",
								modal: true,
								resizable: false,
								draggable: false
							});

							$('#gencode').dialog('open');

							$.ajax({
								type: "POST",
								data: {id: id},
								url: "includes/ol/generate_code.php",
								cache:false
							}).done(function(stuff){
								$("#gencode").html(stuff);
							});
						}
						</script>

						<span style="position:absolute; right:0px;">						<div id="fb-root"></div>
				<script>(function(d, s, id) {
						  var js, fjs = d.getElementsByTagName(s)[0];
						  if (d.getElementById(id)) {return;}
						  js = d.createElement(s); js.id = id;
						  js.src = "//connect.facebook.net/en_US/all.js#appId=175566165856458&xfbml=1";
						  fjs.parentNode.insertBefore(js, fjs);
						}(document, 'script', 'facebook-jssdk'));
				</script>
						<div class="fb-like" data-width="50" data-href="http://flightrising.com/main.php?dragon=21304374" data-send="false" data-layout="button_count" data-width="30" data-show-faces="false" data-action="like" data-font="arial"> </div>						</span>
				</div>
			</fieldset>
		</div>

		<div class="clear" style="height:5px;"></div>

		<div style="float:left; width:230px; margin-right:15px; margin-bottom:10px;">
		<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; height:293px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-top:10px; text-align:center;">Apparel & Skins</div>
			<div style="width:200px; height:200px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:5px; background-color:#EEE; border:solid 1px #BBB; overflow-x:hidden; overflow-y:scroll;">
						</div>
			<div style="text-align:center;">
								<a class="loginbar" title="This dragon is too young to wear skins or accents."><img src="http://flightrising.com/images/layout/button_skins_inactive.png" border="0"></a>

					<a class="loginbar" title="This dragon is too young to wear apparel."><img src="http://flightrising.com/images/layout/button_apparel_inactive.png" border="0"></a>
								</div>
		</fieldset>
		<script type="text/javascript">

		function appPrev(itemid){
			$('body').append('<div id="itemprev"></div>');
			$("#itemprev").html('<img src="/images/layout/loading.gif"> loading...');

			$('#itemprev').dialog({
				autoOpen: false,
				title: "Preview Apparel",
				width: 320,
				height: "auto",
				modal: true,
				resizable: false,
				draggable: false,
				closeOnEscape: false,
				position: ["center", 100],
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
				}
			});

			$('#itemprev').dialog('open');

			$.ajax({
				type: "POST",
				data: {itemid: itemid},
				url: "includes/ol/item_preview.php",
				cache:false
			}).done(function(stuff){
				$("#itemprev").html(stuff);
			});
		}

		function skinPrev(itemid)
		{
			$('body').append('<div id="skinprev"></div>');
			$("#skinprev").html('<img src="/images/layout/loading.gif"> loading...');

			$('#skinprev').dialog({
				autoOpen: false,
				title: "Preview Skin #"+itemid,
				width: 470,
				height: "auto",
				modal: true,
				resizable: false,
				draggable: false,
				closeOnEscape: false,
				position: ["center", 100],
				open: function(event, ui) {
					$(".ui-dialog-titlebar-close", ui.dialog).hide();
				}
			});

			$('#skinprev').dialog('open');

			$.ajax({
				type: "POST",
				data: {id: itemid, page: "1"},
				url: "includes/ol/skinprev.php",
				cache:false
			}).done(function(stuff){
				$("#skinprev").html(stuff);
			});
		}
		</script>
		</div>

		<div style="float:left; width:210px; margin-right:15px; margin-bottom:10px;">
		<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; height:293px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-top:10px; text-align:center;">Lineage</div>

			<div style="width:180px; height:200px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:5px; background-color:#EEE; border:solid 1px #BBB; overflow:auto;">

			<div style="color:#76240f; font-size:12px; font-weight:bold; margin-left:10px; margin-top:10px;">Parents</div>
			<div style="margin-left:25px;">
			<a href=main.php?p=lair&id=95470&tab=dragon&did=6930512 style="color:#000; font-weight:bold; text-decoration:underline;">Terrorbone</a>
					<br />
 					<a href=main.php?p=lair&id=95470&tab=dragon&did=6930511 style="color:#000; font-weight:bold; text-decoration:underline;">Gemstone</a>			</div>

			<div style="width:160px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:10px;"><img src="/images/layout/graydot.gif" width="160" height="1" /></div>

			<div style="color:#76240f; font-size:12px; font-weight:bold; margin-left:10px; margin-top:10px;">Offspring</div>
			<div style="margin-left:25px;">
			<em>none</em>			</div>


            <div style="width:160px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:10px;"><img src="/images/layout/graydot.gif" width="160" height="1" /></div>

			<span id="exalts">
			            </span>




            </div>
			<div style="text-align:center;">
            				<a class="loginbar" title="This dragon is unable to breed right now."><img border="0" src="http://flightrising.com/images/layout/breed_inactive.png"></a>
								<a class="loginbar" TITLE="This dragon will not be available to breed for 14 days."><img border="0" src="/images/icons/breeding_cooldown.png"  /></a>
				            </div>
		</fieldset>
		</div>

		<div style="float:left; width:230px; margin-bottom:10px;;">
		<fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; height:293px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-top:10px; text-align:center;">Familiar</div>

			<div style="width:205px; height:205px; margin-left:auto; margin-right:auto; margin-top:10px; margin-bottom:5px; background-color:#EEE; border:solid 1px #BBB; overflow:auto;">
						</div>
			<div style="text-align:center;">
							<a class="loginbar" title="Click this button to change what familiar is paired with this dragon." href="main.php?p=lair&id=95470&tab=familiar&did=21304374" /><img border="0" src="http://flightrising.com/images/layout/button_change.png" style="vertical-align:middle;"></a>
							</div>
		</fieldset>
		</div>

		<div class="clear" style="width:700px;">
		<a name="bio"><fieldset style="margin:0px; border:solid 1px #000; background-color:#dad6c8; -moz-border-radius:1em; -khtml-border-radius:1em; -webkit-border-radius:1em; border-radius:1em; min-height:263px; padding:10px;">
			<div style="color:#731d08; font-weight:bold; font-size:12px; margin-left:auto; margin-right:auto; width:200px; margin-bottom:15px; text-align:center;">Information</div>


		<div style="color: #000000; font-size: 12px; width:640px; overflow:auto; min-height:160px; margin-left:auto; margin-right:auto; background-color:#EEE; border:solid 1px #BBB; padding:20px;">

        </div>
					<div style="text-align:center;"><form method="post" action="main.php?p=lair&id=95470&tab=dragon&did=21304374&action=edit#bio"><input type="submit" value="Edit" class="mb_button" onclick="" /></form></div>
				</fieldset></a>
		<br>&nbsp;



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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456205365' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456205365' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456205365&amp;n=a26545c2' border='0' alt='' /></a></iframe>
		<script type='text/javascript' src='http://162.218.115.228/delivery/ag.php'></script>

		</div></div>
<!--End Bottom Banner-->
<div class="copybar">&copy; 2013 Stormlight Workshop. All Rights Reserved<br />
<a href="main.php?p=tos">Terms of Use</a> | <a href="http://flightrising.com/main.php?board=frd&id=749441&p=mb">Rules and Guidelines</a> | <a href="main.php?p=privacy">Privacy Policy</a> | <a href="main.php?p=credits">Credits</a> |  <a href="index.php?p=contact">Contact Us</a> | <a href="http://www.virtualpetlist.com/" target="_blank" alt="Virtual Pet List">Virtual Pets Forum</a></div>
<!--End Copybar-->

<!--End Container-->
</div>

	<script type="text/javascript">
	</script>

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