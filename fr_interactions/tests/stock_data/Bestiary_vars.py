LOGGED_IN_BESTIARY_PAGE_1 = """
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



<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-45423708-1', 'flightrising.com', 'ls');
  ga('create', 'UA-3549204-2', 'flightrising.com');
  ga('require', 'displayfeatures');
  ga('ls.send', 'pageview');
  ga('send', 'pageview');

</script>
</head>




	<body style="background-image: url(/images/layout/none/bg.jpg);">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/holiday_9/banner.jpg); position:relative;">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	10:37    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">3633 Users Online</a></strong>
	</span>

	<!--Food-->
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
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 331	</a>

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

                	<span id="user_treasure" style="font-size:11px;">1530523</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3067</span>
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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456079858' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456079858' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456079858&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
		<a href="main.php?p=lair&tab=userpage&id=95470" style="color:#000;">Clan Profile</a> &raquo;
	<a href="main.php?p=bestiary" style="color:#731d08; font-weight:bold;">Bestiary</a>
</div>


<div style="position:relative; text-align:right; width:705px; height:69px; margin-left:15px; margin-bottom:20px;">
	<span style="font-size:22px; color:#731d08; font-weight:bold; position:absolute; top:20px; left:0px;">Bestiary</span>

	<div style="color:#666; font-size:12px; position:absolute; bottom:10px; left:0px;">
		Chronicles of the beasts you have encountered and collected!
	</div>

	<span style="position:absolute; bottom:25px; right:0px;">
		<span style="margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#731d08; font-weight:bold;" href="main.php?p=bestiary&tab=familiars">Familiars (331)</a>
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
			<img src="/images/cms/familiar/art/4350.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Abyss Striker</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These observers cluster around ancient aquatic ruins. They may change color to blend with their surroundings.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
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
			<img src="/images/cms/familiar/art/15298.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Agol</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">A backwards thinking creature.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty4.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Companion</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13435.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Almandine Sturgeon</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Dwelling in the waters of the Crystal Pools has left the scales of this fish translucent and hard as a gemstone.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/376.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Amaranth Moth</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">This distinctive moth has deep reds and purples running through it's leafy wings. Its difficult to classify as purely flora or fauna.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13434.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Amber Gulper</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Sometimes dragon eats fish. Sometimes fish eats dragon.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/12739.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Amberwing Waveskimmer</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These avians are always humming. It's incredibly annoying.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty1.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Tolerant</div>
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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456079858' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456079858' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456079858&amp;n=a26545c2' border='0' alt='' /></a></iframe>
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

PARSED_BESTIARY_PAGE_1 = [{'src': u'/images/cms/familiar/art/4350.png', 'loyalty': u'Awakened', 'id': u'4350', 'name': u'Abyss Striker'}, {'src': u'/images/cms/familiar/art/16261_gray.png', 'loyalty': u'Locked', 'id': u'16261', 'name': u'Acid-Tongue Serpenta'}, {'src': u'/images/cms/familiar/art/16489_gray.png', 'loyalty': u'Locked', 'id': u'16489', 'name': u'Aer Phantom'}, {'src': u'/images/cms/familiar/art/15298.png', 'loyalty': u'Companion', 'id': u'15298', 'name': u'Agol'}, {'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Awakened', 'id': u'13435', 'name': u'Almandine Sturgeon'}, {'src': u'/images/cms/familiar/art/376.png', 'loyalty': u'Awakened', 'id': u'376', 'name': u'Amaranth Moth'}, {'src': u'/images/cms/familiar/art/13434.png', 'loyalty': u'Awakened', 'id': u'13434', 'name': u'Amber Gulper'}, {'src': u'/images/cms/familiar/art/12739.png', 'loyalty': u'Tolerant', 'id': u'12739', 'name': u'Amberwing Waveskimmer'}]

BREAKDOWN_BESTIARY_PAGE_1 = {'taming': [{'src': u'/images/cms/familiar/art/15298.png', 'loyalty': u'Companion', 'id': u'15298', 'name': u'Agol'}, {'src': u'/images/cms/familiar/art/12739.png', 'loyalty': u'Tolerant', 'id': u'12739', 'name': u'Amberwing Waveskimmer'}], 'awakened': [{'src': u'/images/cms/familiar/art/4350.png', 'loyalty': u'Awakened', 'id': u'4350', 'name': u'Abyss Striker'}, {'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Awakened', 'id': u'13435', 'name': u'Almandine Sturgeon'}, {'src': u'/images/cms/familiar/art/376.png', 'loyalty': u'Awakened', 'id': u'376', 'name': u'Amaranth Moth'}, {'src': u'/images/cms/familiar/art/13434.png', 'loyalty': u'Awakened', 'id': u'13434', 'name': u'Amber Gulper'}], 'bestiary': [{'src': u'/images/cms/familiar/art/4350.png', 'loyalty': u'Awakened', 'id': u'4350', 'name': u'Abyss Striker'}, {'src': u'/images/cms/familiar/art/16261_gray.png', 'loyalty': u'Locked', 'id': u'16261', 'name': u'Acid-Tongue Serpenta'}, {'src': u'/images/cms/familiar/art/16489_gray.png', 'loyalty': u'Locked', 'id': u'16489', 'name': u'Aer Phantom'}, {'src': u'/images/cms/familiar/art/15298.png', 'loyalty': u'Companion', 'id': u'15298', 'name': u'Agol'}, {'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Awakened', 'id': u'13435', 'name': u'Almandine Sturgeon'}, {'src': u'/images/cms/familiar/art/376.png', 'loyalty': u'Awakened', 'id': u'376', 'name': u'Amaranth Moth'}, {'src': u'/images/cms/familiar/art/13434.png', 'loyalty': u'Awakened', 'id': u'13434', 'name': u'Amber Gulper'}, {'src': u'/images/cms/familiar/art/12739.png', 'loyalty': u'Tolerant', 'id': u'12739', 'name': u'Amberwing Waveskimmer'}], 'locked': [{'src': u'/images/cms/familiar/art/16261_gray.png', 'loyalty': u'Locked', 'id': u'16261', 'name': u'Acid-Tongue Serpenta'}, {'src': u'/images/cms/familiar/art/16489_gray.png', 'loyalty': u'Locked', 'id': u'16489', 'name': u'Aer Phantom'}]}


BEAST_SPAN = """<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">
<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
<img height="140" src="/images/cms/familiar/art/4350.png" width="140"/>
</div>
<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Abyss Striker</div>
<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These observers cluster around ancient aquatic ruins. They may change color to blend with their surroundings.</div>
</div>
<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png"/><img src="/images/layout/loyalty6.png"/></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
</span>"""

PARSED_BEAST_SPAN = {'src': u'/images/cms/familiar/art/4350.png', 'loyalty': u'Awakened', 'id': u'4350', 'name': u'Abyss Striker'}

BAD_BESTIARY_PAGE = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
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



<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-45423708-1', 'flightrising.com', 'ls');
  ga('create', 'UA-3549204-2', 'flightrising.com');
  ga('require', 'displayfeatures');
  ga('ls.send', 'pageview');
  ga('send', 'pageview');

</script>
</head>




	<body style="background-image: url(/images/layout/none/bg.jpg);">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/holiday_9/banner.jpg); position:relative;">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	10:37    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">3633 Users Online</a></strong>
	</span>

	<!--Food-->
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
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 331	</a>

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

                	<span id="user_treasure" style="font-size:11px;">1530523</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3067</span>
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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456079858' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456079858' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456079858&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
		<a href="main.php?p=lair&tab=userpage&id=95470" style="color:#000;">Clan Profile</a> &raquo;
	<a href="main.php?p=bestiary" style="color:#731d08; font-weight:bold;">Bestiary</a>
</div>


<div style="position:relative; text-align:right; width:705px; height:69px; margin-left:15px; margin-bottom:20px;">
	<span style="font-size:22px; color:#731d08; font-weight:bold; position:absolute; top:20px; left:0px;">Bestiary</span>

	<div style="color:#666; font-size:12px; position:absolute; bottom:10px; left:0px;">
		Chronicles of the beasts you have encountered and collected!
	</div>

	<span style="position:absolute; bottom:25px; right:0px;">
		<span style="margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#731d08; font-weight:bold;" href="main.php?p=bestiary&tab=familiars">Familiars (331)</a>
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
			<img src="/images/cms/familiar/art/4350.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;"></div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These observers cluster around ancient aquatic ruins. They may change color to blend with their surroundings.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456079858' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456079858' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456079858&amp;n=a26545c2' border='0' alt='' /></a></iframe>
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

BESTIARY_PAGE_1_OF_3 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flight Rising (1)</title>

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
	<div class="banner" style="background-image:url(/images/layout/holiday_9/banner.jpg); position:relative;">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	15:14    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">3408 Users Online</a></strong>
	</span>

	<!--Food-->
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
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; background-image:url(images/layout/alert_box_bg.png); color:#FFF;">
				1			</div>
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
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 331	</a>

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

                	<span id="user_treasure" style="font-size:11px;">1796823</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3067</span>
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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456096446' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456096446' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456096446&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
		<a href="main.php?p=lair&tab=userpage&id=95470" style="color:#000;">Clan Profile</a> &raquo;
	<a href="main.php?p=bestiary" style="color:#731d08; font-weight:bold;">Bestiary</a>
</div>


<div style="position:relative; text-align:right; width:705px; height:69px; margin-left:15px; margin-bottom:20px;">
	<span style="font-size:22px; color:#731d08; font-weight:bold; position:absolute; top:20px; left:0px;">Bestiary</span>

	<div style="color:#666; font-size:12px; position:absolute; bottom:10px; left:0px;">
		Chronicles of the beasts you have encountered and collected!
	</div>

	<span style="position:absolute; bottom:25px; right:0px;">
		<span style="margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#731d08; font-weight:bold;" href="main.php?p=bestiary&tab=familiars">Familiars (332)</a>
		</span>
		<!--|
		<span style="margin-left:25px; margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#777777;" href="main.php?p=bestiary&tab=enemies">Enemies (0)</a>
		</span>	-->
	</span>
</div>



<div style="width:700px; margin-left:auto; margin-right:auto;">
	<div style="width:700px; margin-left:auto; margin-right:auto; text-align:center;">
	<div style="width:670px; margin-left:auto; margin-right:auto; text-align:center; margin-bottom:15px; font-size:12px;"><img border="0" src="/images/layout/arrow_left_off.png" style="vertical-align:middle; position:absolute; left:25px;" /> <span style="font-weight:bold;">1</span> <a href='main.php?p=bestiary&tab=familiars&page=2'>2</a> <a href='main.php?p=bestiary&tab=familiars&page=3'>3</a><a href="main.php?p=bestiary&tab=familiars&page=2"><img border="0" src="/images/layout/arrow_right.png" style="cursor:pointer; vertical-align:middle; position:absolute; right:25px;" /></a> </div>
			<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/4350.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Abyss Striker</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These observers cluster around ancient aquatic ruins. They may change color to blend with their surroundings.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
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
			<img src="/images/cms/familiar/art/15298.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Agol</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">A backwards thinking creature.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty4.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Companion</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13435.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Almandine Sturgeon</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Dwelling in the waters of the Crystal Pools has left the scales of this fish translucent and hard as a gemstone.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/376.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Amaranth Moth</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">This distinctive moth has deep reds and purples running through it's leafy wings. Its difficult to classify as purely flora or fauna.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13434.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Amber Gulper</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Sometimes dragon eats fish. Sometimes fish eats dragon.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/12739.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Amberwing Waveskimmer</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These avians are always humming. It's incredibly annoying.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty1.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Tolerant</div>
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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456096446' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456096446' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456096446&amp;n=a26545c2' border='0' alt='' /></a></iframe>
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

BESTIARY_PAGE_2_OF_3 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flight Rising (10)</title>

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
			sel.text = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=2&id=0#"+id+"']"+quote+"[/quote]";
		}

		else
    	{  // Code for Mozilla Firefox
			var len = textarea.value.length;
	    	var start = textarea.selectionStart;
			var end = textarea.selectionEnd;


			var scrollTop = textarea.scrollTop;
			var scrollLeft = textarea.scrollLeft;


        	var sel = textarea.value.substring(start, end);
			var rep = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=2&id=0#"+id+"']"+quote+"[/quote]";
        	textarea.value =  textarea.value.substring(0,start) + rep + textarea.value.substring(end,len);

			textarea.scrollTop = scrollTop;
			textarea.scrollLeft = scrollLeft;
		}
	}
</script>



</head>




	<body style="background-image: url(/images/layout/none/bg.jpg);">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/holiday_9/banner.jpg); position:relative;">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	14:25    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">3631 Users Online</a></strong>
	</span>

	<!--Food-->
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
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; background-image:url(images/layout/alert_box_bg.png); color:#FFF;">
				10			</div>
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
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 331	</a>

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

                	<span id="user_treasure" style="font-size:11px;">1530523</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3067</span>
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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456093518' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456093518' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456093518&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
		<a href="main.php?p=lair&tab=userpage&id=95470" style="color:#000;">Clan Profile</a> &raquo;
	<a href="main.php?p=bestiary" style="color:#731d08; font-weight:bold;">Bestiary</a>
</div>


<div style="position:relative; text-align:right; width:705px; height:69px; margin-left:15px; margin-bottom:20px;">
	<span style="font-size:22px; color:#731d08; font-weight:bold; position:absolute; top:20px; left:0px;">Bestiary</span>

	<div style="color:#666; font-size:12px; position:absolute; bottom:10px; left:0px;">
		Chronicles of the beasts you have encountered and collected!
	</div>

	<span style="position:absolute; bottom:25px; right:0px;">
		<span style="margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#731d08; font-weight:bold;" href="main.php?p=bestiary&tab=familiars">Familiars (331)</a>
		</span>
		<!--|
		<span style="margin-left:25px; margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#777777;" href="main.php?p=bestiary&tab=enemies">Enemies (0)</a>
		</span>	-->
	</span>
</div>



<div style="width:700px; margin-left:auto; margin-right:auto;">
	<div style="width:700px; margin-left:auto; margin-right:auto; text-align:center;">
	<div style="width:670px; margin-left:auto; margin-right:auto; text-align:center; margin-bottom:15px; font-size:12px;"><a href="main.php?p=bestiary&tab=familiars&page=1"><img border="0" src="/images/layout/arrow_left.png" style="cursor:pointer; vertical-align:middle; position:absolute; left:25px;" /></a> <a href='main.php?p=bestiary&tab=familiars&page=1'>1</a> <span style="font-weight:bold;">2</span> <a href='main.php?p=bestiary&tab=familiars&page=3'>3</a><a href="main.php?p=bestiary&tab=familiars&page=3"><img border="0" src="/images/layout/arrow_right.png" style="cursor:pointer; vertical-align:middle; position:absolute; right:25px;" /></a> </div>
			<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/16249_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Amethyst King</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Warped by unstable energies, these arcane-infused ursidae lose all sense of reason when angered. (Colored by LadyKianna.)</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/356.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Ancient Fungus</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">The most crotchety of fungi. As it ages the outer shell becomes crackled and hard as stone.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/15280.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Animated Statue</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">This peculiar statue wasn't standing there when you last looked, and it certainly wasn't posed in that way either. Don't turn your back. Don't look away.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty4.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Companion</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/12194.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Anomalous Skink</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Two heads are better than one, except when they're connected to two stomachs. Food fight!</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty4.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Companion</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13433.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Apatite Fisher</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Feasting a diet of crystal-scaled fish has had a dramatic effect on the plumage of this crane.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/1779_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Arcane Sprite</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Entourage of the Arcanist. (Starfall Celebration Holiday Familiar 2013.)</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/13432.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Arctic Hippalectryon</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">This Hippalectryon emits a frigid aura.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/358.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Autumn Dryad</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">The autumn dryad is often seen guiding local fauna to burrows or caves so that they are protected from the approaching colds of winter.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456093518' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456093518' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456093518&amp;n=a26545c2' border='0' alt='' /></a></iframe>
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

BESTIARY_PAGE_3_OF_3 = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flight Rising (1)</title>

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
			sel.text = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=3&id=0#"+id+"']"+quote+"[/quote]";
		}

		else
    	{  // Code for Mozilla Firefox
			var len = textarea.value.length;
	    	var start = textarea.selectionStart;
			var end = textarea.selectionEnd;


			var scrollTop = textarea.scrollTop;
			var scrollLeft = textarea.scrollLeft;


        	var sel = textarea.value.substring(start, end);
			var rep = "[quote name='"+user+"' date='"+date+"' url='main.php?p=mb&board=&page=3&id=0#"+id+"']"+quote+"[/quote]";
        	textarea.value =  textarea.value.substring(0,start) + rep + textarea.value.substring(end,len);

			textarea.scrollTop = scrollTop;
			textarea.scrollLeft = scrollLeft;
		}
	}
</script>



</head>




	<body style="background-image: url(/images/layout/none/bg.jpg);">
	<div class="container">
	<div class="banner" style="background-image:url(/images/layout/holiday_9/banner.jpg); position:relative;">


<div class="logo" id="logo" style="width:325px;"><a href="http://flightrising.com/index.php"><img border="0" src="/images/layout/trans.png" width="312" height="140" /></a></div>







<div style="position:absolute; left:725px; bottom:70px; color: #e8cc9f;"></div>

<div class="loginarea" id="loginarea">



<div style="position:absolute; height:27px; width:950px; bottom:4px; right:0px;">



  	<span style="position:absolute; top:8px; left:10px; text-align:left; vertical-align:middle;">
	<span style="position:relative; margin-right:15px; font-weight:bold; display:inline-block;">
    <img src="/images/layout/siteclock.png" style="vertical-align:middle;">
	15:14    </span>
    |
	</span>

	<span style="position:absolute; top:8px; left:100px; text-align:left;">
	<strong><a href="main.php?p=active" class="loginlinks">3664 Users Online</a></strong>
	</span>

	<!--Food-->
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
			<div style="width:21px; height:16px; text-align:center; position:relative; padding-top:3px; background-image:url(images/layout/alert_box_bg.png); color:#FFF;">
				1			</div>
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
	<img src="/images/layout/icon_bestiary.png" width="25" height="25" border="0" align="absmiddle" /> 331	</a>

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

                	<span id="user_treasure" style="font-size:11px;">1796823</span>
			        </a>
	</span>

	<span style="text-align:left; cursor:default; display:inline-block; position:absolute; left:90px; bottom:3px;" >
		<a class="loginlinks loginbar" title="Gems are used to upgrade your account and purchase special items." onclick="window.location='main.php?p=ge'" style="color:#731d08; cursor:pointer;">
		<img src="/images/layout/icon_gems.png" width="20" height="20" border="0" align="absmiddle" style="cursor:pointer;">
		<span id="user_gems" style="font-size:11px;">3067</span>
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

		<iframe id='a7fdc708' name='a7fdc708' src='http://162.218.115.228/delivery/afr.php?n=a7fdc708&amp;zoneid=63&amp;target=_blank&amp;cb=1456096492' frameborder='0' scrolling='no' width='160' height='600'><a href='http://162.218.115.228/delivery/ck.php?n=a45ba4b0&amp;cb=1456096492' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=63&amp;cb=1456096492&amp;n=a45ba4b0' border='0' alt='' /></a></iframe>
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
		<a href="main.php?p=lair&tab=userpage&id=95470" style="color:#000;">Clan Profile</a> &raquo;
	<a href="main.php?p=bestiary" style="color:#731d08; font-weight:bold;">Bestiary</a>
</div>


<div style="position:relative; text-align:right; width:705px; height:69px; margin-left:15px; margin-bottom:20px;">
	<span style="font-size:22px; color:#731d08; font-weight:bold; position:absolute; top:20px; left:0px;">Bestiary</span>

	<div style="color:#666; font-size:12px; position:absolute; bottom:10px; left:0px;">
		Chronicles of the beasts you have encountered and collected!
	</div>

	<span style="position:absolute; bottom:25px; right:0px;">
		<span style="margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#731d08; font-weight:bold;" href="main.php?p=bestiary&tab=familiars">Familiars (332)</a>
		</span>
		<!--|
		<span style="margin-left:25px; margin-right:25px;">
		<a class="treeNode_default" style="font-size:11px;color:#777777;" href="main.php?p=bestiary&tab=enemies">Enemies (0)</a>
		</span>	-->
	</span>
</div>



<div style="width:700px; margin-left:auto; margin-right:auto;">
	<div style="width:700px; margin-left:auto; margin-right:auto; text-align:center;">
	<div style="width:670px; margin-left:auto; margin-right:auto; text-align:center; margin-bottom:15px; font-size:12px;"><a href="main.php?p=bestiary&tab=familiars&page=2"><img border="0" src="/images/layout/arrow_left.png" style="cursor:pointer; vertical-align:middle; position:absolute; left:25px;" /></a> <a href='main.php?p=bestiary&tab=familiars&page=1'>1</a> <a href='main.php?p=bestiary&tab=familiars&page=2'>2</a> <span style="font-weight:bold;">3</span><img border="0" src="/images/layout/arrow_right_off.png" style="cursor:pointer; vertical-align:middle; position:absolute; right:25px;" /> </div>
			<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/14289_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Autumn Sea Dragon</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These creatures will conceal themselves among sea grasses, adding a touch of autumn color to underwater fields of green.</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/405.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Baku</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Baku are able to walk both the physical and ethereal plane.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/1149.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Bamboo Phytocat</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Little is known about how the Bamboo Phytocat's physiology evolved, but one thing is for certain: watch the reeds as you walk.. (KS-sponsored by kiohl.)</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/600.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Banded Owlcat</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">The banded owlcat moves silently, both in the air and on the ground.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/10666.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Barkback Boar</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">These animated guardians grow from fallen trees.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/16254_gray.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#B6B6B6; width:130px; margin-left:auto; margin-right:auto;">Barking Jester</div>
				<div style="color:#B6B6B6; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Always thrilled to play, this bright canine is the perfect distraction for a lair full of tireless hatchlings. (Colored by Cynderbark.)</div>
			</div>

			<div style="position:absolute; right:10px; bottom:8px; color:#888; font-style:italic; font-weight:bold;">Locked</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/381.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Basilisk</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">A basilisk's gaze can petrify even the hardiest Earth dragons into stone. Staring contests with this familiar are not recommended.</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /><img src="/images/layout/loyalty6.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Awakened</div>
		</span>
				<span style="height:300px; width:160px; border:1px solid #000; display:inline-block; -moz-border-radius:12px; -khtml-border-radius:12px; -webkit-border-radius:12px; border-radius:12px; text-align:center; margin-top:10px; margin-right:10px; background-color:#dad6c8; position:relative;">

			<div style="width:140px; height:140px; margin-left:auto; margin-right:auto; margin-top:5px;">
			<img src="/images/cms/familiar/art/16244.png" height="140" width="140" />
			</div>

			<div style="width:140px; height:120px; left:10px; top:150px; background-color:#fff; border:1px solid #aaa; position:absolute;">
				<div style="font-size:11px; font-weight:bold; color:#731d08; width:130px; margin-left:auto; margin-right:auto;">Bearded Yeti</div>
				<div style="color:#000; width:130px; text-align:left; margin-top:5px; margin-left:auto; margin-right:auto;">Never surrender. Never shave. (Colored by Akitaxzero.)</div>
			</div>

			<div style="position:absolute; bottom:5px; left:10px;"><img src="/images/layout/net.png" /></div><div style="position:absolute; right:10px; bottom:8px; color:#731d08; font-style:italic; font-weight:bold;">Wary</div>
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

		<iframe id='a85acf58' name='a85acf58' src='http://162.218.115.228/delivery/afr.php?n=a85acf58&amp;zoneid=61&amp;target=_blank&amp;cb=1456096492' frameborder='0' scrolling='no' width='728' height='90'><a href='http://162.218.115.228/delivery/ck.php?n=a26545c2&amp;cb=1456096492' target='_blank'><img src='http://162.218.115.228/delivery/avw.php?zoneid=61&amp;cb=1456096492&amp;n=a26545c2' border='0' alt='' /></a></iframe>
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

BREAKDOWN_PAGE_1_TO_3 = {'taming': [{'src': u'/images/cms/familiar/art/15298.png', 'loyalty': u'Companion', 'id': u'15298', 'name': u'Agol'}, {'src': u'/images/cms/familiar/art/12739.png', 'loyalty': u'Tolerant', 'id': u'12739', 'name': u'Amberwing Waveskimmer'}, {'src': u'/images/cms/familiar/art/15280.png', 'loyalty': u'Companion', 'id': u'15280', 'name': u'Animated Statue'}, {'src': u'/images/cms/familiar/art/12194.png', 'loyalty': u'Companion', 'id': u'12194', 'name': u'Anomalous Skink'}, {'src': u'/images/cms/familiar/art/16244.png', 'loyalty': u'Wary', 'id': u'16244', 'name': u'Bearded Yeti'}], 'awakened': [{'src': u'/images/cms/familiar/art/4350.png', 'loyalty': u'Awakened', 'id': u'4350', 'name': u'Abyss Striker'}, {'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Awakened', 'id': u'13435', 'name': u'Almandine Sturgeon'}, {'src': u'/images/cms/familiar/art/376.png', 'loyalty': u'Awakened', 'id': u'376', 'name': u'Amaranth Moth'}, {'src': u'/images/cms/familiar/art/13434.png', 'loyalty': u'Awakened', 'id': u'13434', 'name': u'Amber Gulper'}, {'src': u'/images/cms/familiar/art/356.png', 'loyalty': u'Awakened', 'id': u'356', 'name': u'Ancient Fungus'}, {'src': u'/images/cms/familiar/art/13433.png', 'loyalty': u'Awakened', 'id': u'13433', 'name': u'Apatite Fisher'}, {'src': u'/images/cms/familiar/art/13432.png', 'loyalty': u'Awakened', 'id': u'13432', 'name': u'Arctic Hippalectryon'}, {'src': u'/images/cms/familiar/art/358.png', 'loyalty': u'Awakened', 'id': u'358', 'name': u'Autumn Dryad'}, {'src': u'/images/cms/familiar/art/405.png', 'loyalty': u'Awakened', 'id': u'405', 'name': u'Baku'}, {'src': u'/images/cms/familiar/art/1149.png', 'loyalty': u'Awakened', 'id': u'1149', 'name': u'Bamboo Phytocat'}, {'src': u'/images/cms/familiar/art/600.png', 'loyalty': u'Awakened', 'id': u'600', 'name': u'Banded Owlcat'}, {'src': u'/images/cms/familiar/art/10666.png', 'loyalty': u'Awakened', 'id': u'10666', 'name': u'Barkback Boar'}, {'src': u'/images/cms/familiar/art/381.png', 'loyalty': u'Awakened', 'id': u'381', 'name': u'Basilisk'}], 'bestiary': [{'src': u'/images/cms/familiar/art/4350.png', 'loyalty': u'Awakened', 'id': u'4350', 'name': u'Abyss Striker'}, {'src': u'/images/cms/familiar/art/16261_gray.png', 'loyalty': u'Locked', 'id': u'16261', 'name': u'Acid-Tongue Serpenta'}, {'src': u'/images/cms/familiar/art/16489_gray.png', 'loyalty': u'Locked', 'id': u'16489', 'name': u'Aer Phantom'}, {'src': u'/images/cms/familiar/art/15298.png', 'loyalty': u'Companion', 'id': u'15298', 'name': u'Agol'}, {'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Awakened', 'id': u'13435', 'name': u'Almandine Sturgeon'}, {'src': u'/images/cms/familiar/art/376.png', 'loyalty': u'Awakened', 'id': u'376', 'name': u'Amaranth Moth'}, {'src': u'/images/cms/familiar/art/13434.png', 'loyalty': u'Awakened', 'id': u'13434', 'name': u'Amber Gulper'}, {'src': u'/images/cms/familiar/art/12739.png', 'loyalty': u'Tolerant', 'id': u'12739', 'name': u'Amberwing Waveskimmer'}, {'src': u'/images/cms/familiar/art/16249_gray.png', 'loyalty': u'Locked', 'id': u'16249', 'name': u'Amethyst King'}, {'src': u'/images/cms/familiar/art/356.png', 'loyalty': u'Awakened', 'id': u'356', 'name': u'Ancient Fungus'}, {'src': u'/images/cms/familiar/art/15280.png', 'loyalty': u'Companion', 'id': u'15280', 'name': u'Animated Statue'}, {'src': u'/images/cms/familiar/art/12194.png', 'loyalty': u'Companion', 'id': u'12194', 'name': u'Anomalous Skink'}, {'src': u'/images/cms/familiar/art/13433.png', 'loyalty': u'Awakened', 'id': u'13433', 'name': u'Apatite Fisher'}, {'src': u'/images/cms/familiar/art/1779_gray.png', 'loyalty': u'Locked', 'id': u'1779', 'name': u'Arcane Sprite'}, {'src': u'/images/cms/familiar/art/13432.png', 'loyalty': u'Awakened', 'id': u'13432', 'name': u'Arctic Hippalectryon'}, {'src': u'/images/cms/familiar/art/358.png', 'loyalty': u'Awakened', 'id': u'358', 'name': u'Autumn Dryad'}, {'src': u'/images/cms/familiar/art/14289_gray.png', 'loyalty': u'Locked', 'id': u'14289', 'name': u'Autumn Sea Dragon'}, {'src': u'/images/cms/familiar/art/405.png', 'loyalty': u'Awakened', 'id': u'405', 'name': u'Baku'}, {'src': u'/images/cms/familiar/art/1149.png', 'loyalty': u'Awakened', 'id': u'1149', 'name': u'Bamboo Phytocat'}, {'src': u'/images/cms/familiar/art/600.png', 'loyalty': u'Awakened', 'id': u'600', 'name': u'Banded Owlcat'}, {'src': u'/images/cms/familiar/art/10666.png', 'loyalty': u'Awakened', 'id': u'10666', 'name': u'Barkback Boar'}, {'src': u'/images/cms/familiar/art/16254_gray.png', 'loyalty': u'Locked', 'id': u'16254', 'name': u'Barking Jester'}, {'src': u'/images/cms/familiar/art/381.png', 'loyalty': u'Awakened', 'id': u'381', 'name': u'Basilisk'}, {'src': u'/images/cms/familiar/art/16244.png', 'loyalty': u'Wary', 'id': u'16244', 'name': u'Bearded Yeti'}], 'locked': [{'src': u'/images/cms/familiar/art/16261_gray.png', 'loyalty': u'Locked', 'id': u'16261', 'name': u'Acid-Tongue Serpenta'}, {'src': u'/images/cms/familiar/art/16489_gray.png', 'loyalty': u'Locked', 'id': u'16489', 'name': u'Aer Phantom'}, {'src': u'/images/cms/familiar/art/16249_gray.png', 'loyalty': u'Locked', 'id': u'16249', 'name': u'Amethyst King'}, {'src': u'/images/cms/familiar/art/1779_gray.png', 'loyalty': u'Locked', 'id': u'1779', 'name': u'Arcane Sprite'}, {'src': u'/images/cms/familiar/art/14289_gray.png', 'loyalty': u'Locked', 'id': u'14289', 'name': u'Autumn Sea Dragon'}, {'src': u'/images/cms/familiar/art/16254_gray.png', 'loyalty': u'Locked', 'id': u'16254', 'name': u'Barking Jester'}]}

PRINT_TAMING_FOR_BESTIARY_BREAKDOWN = """locked: 104 - [{'src': u'/images/cms/familiar/art/12739_gray.png', 'loyalty': u'Locked', 'name': u'Amberwing Waveskimmer', 'id': u'12739'}, {'src': u'/images/cms/familiar/art/12194_gray.png', 'loyalty': u'Locked', 'name': u'Anomalous Skink', 'id': u'12194'}, {'src': u'/images/cms/familiar/art/1779_gray.png', 'loyalty': u'Locked', 'name': u'Arcane Sprite', 'id': u'1779'}, {'src': u'/images/cms/familiar/art/14289_gray.png', 'loyalty': u'Locked', 'name': u'Autumn Sea Dragon', 'id': u'14289'}, {'src': u'/images/cms/familiar/art/670_gray.png', 'loyalty': u'Locked', 'name': u'Black-wing Hummingbird', 'id': u'670'}, {'src': u'/images/cms/familiar/art/14291_gray.png', 'loyalty': u'Locked', 'name': u'Bloodstone Beetle', 'id': u'14291'}, {'src': u'/images/cms/familiar/art/14547_gray.png', 'loyalty': u'Locked', 'name': u'Blueband Duelist', 'id': u'14547'}, {'src': u'/images/cms/familiar/art/910_gray.png', 'loyalty': u'Locked', 'name': u'Bone Fiend', 'id': u'910'}, {'src': u'/images/cms/familiar/art/591_gray.png', 'loyalty': u'Locked', 'name': u'Boolean', 'id': u'591'}, {'src': u'/images/cms/familiar/art/1222_gray.png', 'loyalty': u'Locked', 'name': u'Coarsefur Yeti', 'id': u'1222'}, {'src': u'/images/cms/familiar/art/760_gray.png', 'loyalty': u'Locked', 'name': u'Cog Frog', 'id': u'760'}, {'src': u'/images/cms/familiar/art/12195_gray.png', 'loyalty': u'Locked', 'name': u'Conjoined Skink', 'id': u'12195'}, {'src': u'/images/cms/familiar/art/14441_gray.png', 'loyalty': u'Locked', 'name': u'Coral Basilisk', 'id': u'14441'}, {'src': u'/images/cms/familiar/art/13430_gray.png', 'loyalty': u'Locked', 'name': u'Crystalhide Jester', 'id': u'13430'}, {'src': u'/images/cms/familiar/art/374_gray.png', 'loyalty': u'Locked', 'name': u'Darktouched Chimera', 'id': u'374'}, {'src': u'/images/cms/familiar/art/642_gray.png', 'loyalty': u'Locked', 'name': u'Downy Fox Rat', 'id': u'642'}, {'src': u'/images/cms/familiar/art/2888_gray.png', 'loyalty': u'Locked', 'name': u'Driftwood Baron', 'id': u'2888'}, {'src': u'/images/cms/familiar/art/635_gray.png', 'loyalty': u'Locked', 'name': u'Dunhoof Ambassador', 'id': u'635'}, {'src': u'/images/cms/familiar/art/2151_gray.png', 'loyalty': u'Locked', 'name': u'Earth Sprite', 'id': u'2151'}, {'src': u'/images/cms/familiar/art/643_gray.png', 'loyalty': u'Locked', 'name': u'Fawn Fox Rat', 'id': u'643'}, {'src': u'/images/cms/familiar/art/1594_gray.png', 'loyalty': u'Locked', 'name': u'Fire Sprite', 'id': u'1594'}, {'src': u'/images/cms/familiar/art/7594_gray.png', 'loyalty': u'Locked', 'name': u'Frost Delver', 'id': u'7594'}, {'src': u'/images/cms/familiar/art/2577_gray.png', 'loyalty': u'Locked', 'name': u'Golden Bantam Fangar', 'id': u'2577'}, {'src': u'/images/cms/familiar/art/919_gray.png', 'loyalty': u'Locked', 'name': u'Golden Idol', 'id': u'919'}, {'src': u'/images/cms/familiar/art/10233_gray.png', 'loyalty': u'Locked', 'name': u'Goldenbeast', 'id': u'10233'}, {'src': u'/images/cms/familiar/art/12740_gray.png', 'loyalty': u'Locked', 'name': u'Great Blue Waveskimmer', 'id': u'12740'}, {'src': u'/images/cms/familiar/art/14442_gray.png', 'loyalty': u'Locked', 'name': u'Grouse Basilisk', 'id': u'14442'}, {'src': u'/images/cms/familiar/art/13428_gray.png', 'loyalty': u'Locked', 'name': u'Hawksbill Goliath', 'id': u'13428'}, {'src': u'/images/cms/familiar/art/355_gray.png', 'loyalty': u'Locked', 'name': u'Hippojay', 'id': u'355'}, {'src': u'/images/cms/familiar/art/2623_gray.png', 'loyalty': u'Locked', 'name': u'Ice Sprite', 'id': u'2623'}, {'src': u'/images/cms/familiar/art/7705_gray.png', 'loyalty': u'Locked', 'name': u'Jadecarved Decoy', 'id': u'7705'}, {'src': u'/images/cms/familiar/art/7702_gray.png', 'loyalty': u'Locked', 'name': u'Lavaborne Hoax', 'id': u'7702'}, {'src': u'/images/cms/familiar/art/975_gray.png', 'loyalty': u'Locked', 'name': u'Light Sprite', 'id': u'975'}, {'src': u'/images/cms/familiar/art/982_gray.png', 'loyalty': u'Locked', 'name': u'Lightning Sprite', 'id': u'982'}, {'src': u'/images/cms/familiar/art/1578_gray.png', 'loyalty': u'Locked', 'name': u'Maned Cobra', 'id': u'1578'}, {'src': u'/images/cms/familiar/art/360_gray.png', 'loyalty': u'Locked', 'name': u'Manticore', 'id': u'360'}, {'src': u'/images/cms/familiar/art/594_gray.png', 'loyalty': u'Locked', 'name': u'Mock Firebird', 'id': u'594'}, {'src': u'/images/cms/familiar/art/11525_gray.png', 'loyalty': u'Locked', 'name': u'Molten Wartoad', 'id': u'11525'}, {'src': u'/images/cms/familiar/art/10231_gray.png', 'loyalty': u'Locked', 'name': u'Overcharged Silverbeast', 'id': u'10231'}, {'src': u'/images/cms/familiar/art/1987_gray.png', 'loyalty': u'Locked', 'name': u'Plague Sprite', 'id': u'1987'}, {'src': u'/images/cms/familiar/art/1313_gray.png', 'loyalty': u'Locked', 'name': u'Red-Footed Akirbeak', 'id': u'1313'}, {'src': u'/images/cms/familiar/art/14288_gray.png', 'loyalty': u'Locked', 'name': u'Seaweed Scavenger', 'id': u'14288'}, {'src': u'/images/cms/familiar/art/2917_gray.png', 'loyalty': u'Locked', 'name': u'Shadow Sprite', 'id': u'2917'}, {'src': u'/images/cms/familiar/art/746_gray.png', 'loyalty': u'Locked', 'name': u'Skycat', 'id': u'746'}, {'src': u'/images/cms/familiar/art/7703_gray.png', 'loyalty': u'Locked', 'name': u'Slumbering Charlatan', 'id': u'7703'}, {'src': u'/images/cms/familiar/art/1573_gray.png', 'loyalty': u'Locked', 'name': u'Speedy', 'id': u'1573'}, {'src': u'/images/cms/familiar/art/1671_gray.png', 'loyalty': u'Locked', 'name': u'Spined Cobra', 'id': u'1671'}, {'src': u'/images/cms/familiar/art/7600_gray.png', 'loyalty': u'Locked', 'name': u'Stone Borer', 'id': u'7600'}, {'src': u'/images/cms/familiar/art/11522_gray.png', 'loyalty': u'Locked', 'name': u'Wartoad', 'id': u'11522'}, {'src': u'/images/cms/familiar/art/3327_gray.png', 'loyalty': u'Locked', 'name': u'Water Sprite', 'id': u'3327'}, {'src': u'/images/cms/familiar/art/7883_gray.png', 'loyalty': u'Locked', 'name': u'Wave Sweeper', 'id': u'7883'}, {'src': u'/images/cms/familiar/art/3148_gray.png', 'loyalty': u'Locked', 'name': u'Wind Sprite', 'id': u'3148'}, {'src': u'/images/cms/familiar/art/12739_gray.png', 'loyalty': u'Locked', 'name': u'Amberwing Waveskimmer', 'id': u'12739'}, {'src': u'/images/cms/familiar/art/12194_gray.png', 'loyalty': u'Locked', 'name': u'Anomalous Skink', 'id': u'12194'}, {'src': u'/images/cms/familiar/art/1779_gray.png', 'loyalty': u'Locked', 'name': u'Arcane Sprite', 'id': u'1779'}, {'src': u'/images/cms/familiar/art/14289_gray.png', 'loyalty': u'Locked', 'name': u'Autumn Sea Dragon', 'id': u'14289'}, {'src': u'/images/cms/familiar/art/670_gray.png', 'loyalty': u'Locked', 'name': u'Black-wing Hummingbird', 'id': u'670'}, {'src': u'/images/cms/familiar/art/14291_gray.png', 'loyalty': u'Locked', 'name': u'Bloodstone Beetle', 'id': u'14291'}, {'src': u'/images/cms/familiar/art/14547_gray.png', 'loyalty': u'Locked', 'name': u'Blueband Duelist', 'id': u'14547'}, {'src': u'/images/cms/familiar/art/910_gray.png', 'loyalty': u'Locked', 'name': u'Bone Fiend', 'id': u'910'}, {'src': u'/images/cms/familiar/art/591_gray.png', 'loyalty': u'Locked', 'name': u'Boolean', 'id': u'591'}, {'src': u'/images/cms/familiar/art/1222_gray.png', 'loyalty': u'Locked', 'name': u'Coarsefur Yeti', 'id': u'1222'}, {'src': u'/images/cms/familiar/art/760_gray.png', 'loyalty': u'Locked', 'name': u'Cog Frog', 'id': u'760'}, {'src': u'/images/cms/familiar/art/12195_gray.png', 'loyalty': u'Locked', 'name': u'Conjoined Skink', 'id': u'12195'}, {'src': u'/images/cms/familiar/art/14441_gray.png', 'loyalty': u'Locked', 'name': u'Coral Basilisk', 'id': u'14441'}, {'src': u'/images/cms/familiar/art/13430_gray.png', 'loyalty': u'Locked', 'name': u'Crystalhide Jester', 'id': u'13430'}, {'src': u'/images/cms/familiar/art/374_gray.png', 'loyalty': u'Locked', 'name': u'Darktouched Chimera', 'id': u'374'}, {'src': u'/images/cms/familiar/art/642_gray.png', 'loyalty': u'Locked', 'name': u'Downy Fox Rat', 'id': u'642'}, {'src': u'/images/cms/familiar/art/2888_gray.png', 'loyalty': u'Locked', 'name': u'Driftwood Baron', 'id': u'2888'}, {'src': u'/images/cms/familiar/art/635_gray.png', 'loyalty': u'Locked', 'name': u'Dunhoof Ambassador', 'id': u'635'}, {'src': u'/images/cms/familiar/art/2151_gray.png', 'loyalty': u'Locked', 'name': u'Earth Sprite', 'id': u'2151'}, {'src': u'/images/cms/familiar/art/643_gray.png', 'loyalty': u'Locked', 'name': u'Fawn Fox Rat', 'id': u'643'}, {'src': u'/images/cms/familiar/art/1594_gray.png', 'loyalty': u'Locked', 'name': u'Fire Sprite', 'id': u'1594'}, {'src': u'/images/cms/familiar/art/7594_gray.png', 'loyalty': u'Locked', 'name': u'Frost Delver', 'id': u'7594'}, {'src': u'/images/cms/familiar/art/2577_gray.png', 'loyalty': u'Locked', 'name': u'Golden Bantam Fangar', 'id': u'2577'}, {'src': u'/images/cms/familiar/art/919_gray.png', 'loyalty': u'Locked', 'name': u'Golden Idol', 'id': u'919'}, {'src': u'/images/cms/familiar/art/10233_gray.png', 'loyalty': u'Locked', 'name': u'Goldenbeast', 'id': u'10233'}, {'src': u'/images/cms/familiar/art/12740_gray.png', 'loyalty': u'Locked', 'name': u'Great Blue Waveskimmer', 'id': u'12740'}, {'src': u'/images/cms/familiar/art/14442_gray.png', 'loyalty': u'Locked', 'name': u'Grouse Basilisk', 'id': u'14442'}, {'src': u'/images/cms/familiar/art/13428_gray.png', 'loyalty': u'Locked', 'name': u'Hawksbill Goliath', 'id': u'13428'}, {'src': u'/images/cms/familiar/art/355_gray.png', 'loyalty': u'Locked', 'name': u'Hippojay', 'id': u'355'}, {'src': u'/images/cms/familiar/art/2623_gray.png', 'loyalty': u'Locked', 'name': u'Ice Sprite', 'id': u'2623'}, {'src': u'/images/cms/familiar/art/7705_gray.png', 'loyalty': u'Locked', 'name': u'Jadecarved Decoy', 'id': u'7705'}, {'src': u'/images/cms/familiar/art/7702_gray.png', 'loyalty': u'Locked', 'name': u'Lavaborne Hoax', 'id': u'7702'}, {'src': u'/images/cms/familiar/art/975_gray.png', 'loyalty': u'Locked', 'name': u'Light Sprite', 'id': u'975'}, {'src': u'/images/cms/familiar/art/982_gray.png', 'loyalty': u'Locked', 'name': u'Lightning Sprite', 'id': u'982'}, {'src': u'/images/cms/familiar/art/1578_gray.png', 'loyalty': u'Locked', 'name': u'Maned Cobra', 'id': u'1578'}, {'src': u'/images/cms/familiar/art/360_gray.png', 'loyalty': u'Locked', 'name': u'Manticore', 'id': u'360'}, {'src': u'/images/cms/familiar/art/594_gray.png', 'loyalty': u'Locked', 'name': u'Mock Firebird', 'id': u'594'}, {'src': u'/images/cms/familiar/art/11525_gray.png', 'loyalty': u'Locked', 'name': u'Molten Wartoad', 'id': u'11525'}, {'src': u'/images/cms/familiar/art/10231_gray.png', 'loyalty': u'Locked', 'name': u'Overcharged Silverbeast', 'id': u'10231'}, {'src': u'/images/cms/familiar/art/1987_gray.png', 'loyalty': u'Locked', 'name': u'Plague Sprite', 'id': u'1987'}, {'src': u'/images/cms/familiar/art/1313_gray.png', 'loyalty': u'Locked', 'name': u'Red-Footed Akirbeak', 'id': u'1313'}, {'src': u'/images/cms/familiar/art/14288_gray.png', 'loyalty': u'Locked', 'name': u'Seaweed Scavenger', 'id': u'14288'}, {'src': u'/images/cms/familiar/art/2917_gray.png', 'loyalty': u'Locked', 'name': u'Shadow Sprite', 'id': u'2917'}, {'src': u'/images/cms/familiar/art/746_gray.png', 'loyalty': u'Locked', 'name': u'Skycat', 'id': u'746'}, {'src': u'/images/cms/familiar/art/7703_gray.png', 'loyalty': u'Locked', 'name': u'Slumbering Charlatan', 'id': u'7703'}, {'src': u'/images/cms/familiar/art/1573_gray.png', 'loyalty': u'Locked', 'name': u'Speedy', 'id': u'1573'}, {'src': u'/images/cms/familiar/art/1671_gray.png', 'loyalty': u'Locked', 'name': u'Spined Cobra', 'id': u'1671'}, {'src': u'/images/cms/familiar/art/7600_gray.png', 'loyalty': u'Locked', 'name': u'Stone Borer', 'id': u'7600'}, {'src': u'/images/cms/familiar/art/11522_gray.png', 'loyalty': u'Locked', 'name': u'Wartoad', 'id': u'11522'}, {'src': u'/images/cms/familiar/art/3327_gray.png', 'loyalty': u'Locked', 'name': u'Water Sprite', 'id': u'3327'}, {'src': u'/images/cms/familiar/art/7883_gray.png', 'loyalty': u'Locked', 'name': u'Wave Sweeper', 'id': u'7883'}, {'src': u'/images/cms/familiar/art/3148_gray.png', 'loyalty': u'Locked', 'name': u'Wind Sprite', 'id': u'3148'}]
awakened: 416
taming: 162
 -- wary: 22 - [{'src': u'/images/cms/familiar/art/14569.png', 'loyalty': u'Wary', 'name': u'Centaur Berserker', 'id': u'14569'}, {'src': u'/images/cms/familiar/art/4679.png', 'loyalty': u'Wary', 'name': u'Chocolate Ferret', 'id': u'4679'}, {'src': u'/images/cms/familiar/art/636.png', 'loyalty': u'Wary', 'name': u'Dappled Dunhoof', 'id': u'636'}, {'src': u'/images/cms/familiar/art/14558.png', 'loyalty': u'Wary', 'name': u'Deepmine Aardvark', 'id': u'14558'}, {'src': u'/images/cms/familiar/art/14290.png', 'loyalty': u'Wary', 'name': u'Empress Beetle', 'id': u'14290'}, {'src': u'/images/cms/familiar/art/9669.png', 'loyalty': u'Wary', 'name': u'Goliath Mountain Beetle', 'id': u'9669'}, {'src': u'/images/cms/familiar/art/10668.png', 'loyalty': u'Wary', 'name': u'Orange Blotch Pansy', 'id': u'10668'}, {'src': u'/images/cms/familiar/art/14560.png', 'loyalty': u'Wary', 'name': u'Peacevine Aardvark', 'id': u'14560'}, {'src': u'/images/cms/familiar/art/14570.png', 'loyalty': u'Wary', 'name': u'Swiftfoot Slayer', 'id': u'14570'}, {'src': u'/images/cms/familiar/art/9668.png', 'loyalty': u'Wary', 'name': u'Tufted Leaf Beetle', 'id': u'9668'}, {'src': u'/images/cms/familiar/art/14546.png', 'loyalty': u'Wary', 'name': u'Venomblade Assassin', 'id': u'14546'}, {'src': u'/images/cms/familiar/art/14569.png', 'loyalty': u'Wary', 'name': u'Centaur Berserker', 'id': u'14569'}, {'src': u'/images/cms/familiar/art/4679.png', 'loyalty': u'Wary', 'name': u'Chocolate Ferret', 'id': u'4679'}, {'src': u'/images/cms/familiar/art/636.png', 'loyalty': u'Wary', 'name': u'Dappled Dunhoof', 'id': u'636'}, {'src': u'/images/cms/familiar/art/14558.png', 'loyalty': u'Wary', 'name': u'Deepmine Aardvark', 'id': u'14558'}, {'src': u'/images/cms/familiar/art/14290.png', 'loyalty': u'Wary', 'name': u'Empress Beetle', 'id': u'14290'}, {'src': u'/images/cms/familiar/art/9669.png', 'loyalty': u'Wary', 'name': u'Goliath Mountain Beetle', 'id': u'9669'}, {'src': u'/images/cms/familiar/art/10668.png', 'loyalty': u'Wary', 'name': u'Orange Blotch Pansy', 'id': u'10668'}, {'src': u'/images/cms/familiar/art/14560.png', 'loyalty': u'Wary', 'name': u'Peacevine Aardvark', 'id': u'14560'}, {'src': u'/images/cms/familiar/art/14570.png', 'loyalty': u'Wary', 'name': u'Swiftfoot Slayer', 'id': u'14570'}, {'src': u'/images/cms/familiar/art/9668.png', 'loyalty': u'Wary', 'name': u'Tufted Leaf Beetle', 'id': u'9668'}, {'src': u'/images/cms/familiar/art/14546.png', 'loyalty': u'Wary', 'name': u'Venomblade Assassin', 'id': u'14546'}]
 -- tolerant: 2 - [{'src': u'/images/cms/familiar/art/14677.png', 'loyalty': u'Tolerant', 'name': u'Granite Guardian', 'id': u'14677'}, {'src': u'/images/cms/familiar/art/14677.png', 'loyalty': u'Tolerant', 'name': u'Granite Guardian', 'id': u'14677'}]
 -- relaxed: 38 - [{'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Relaxed', 'name': u'Almandine Sturgeon', 'id': u'13435'}, {'src': u'/images/cms/familiar/art/13421.png', 'loyalty': u'Relaxed', 'name': u'Maren Warlock', 'id': u'13421'}, {'src': u'/images/cms/familiar/art/1929.png', 'loyalty': u'Relaxed', 'name': u'Mistwatch Shellion', 'id': u'1929'}, {'src': u'/images/cms/familiar/art/6604.png', 'loyalty': u'Relaxed', 'name': u'Nephrite Chameleon', 'id': u'6604'}, {'src': u'/images/cms/familiar/art/905.png', 'loyalty': u'Relaxed', 'name': u'Nightsky Fuiran', 'id': u'905'}, {'src': u'/images/cms/familiar/art/1101.png', 'loyalty': u'Relaxed', 'name': u'Poultrygeist', 'id': u'1101'}, {'src': u'/images/cms/familiar/art/354.png', 'loyalty': u'Relaxed', 'name': u'Scarlet Flycatcher', 'id': u'354'}, {'src': u'/images/cms/familiar/art/1364.png', 'loyalty': u'Relaxed', 'name': u'Scythe Kamaitachi', 'id': u'1364'}, {'src': u'/images/cms/familiar/art/7597.png', 'loyalty': u'Relaxed', 'name': u'Sentinel Mith', 'id': u'7597'}, {'src': u'/images/cms/familiar/art/6332.png', 'loyalty': u'Relaxed', 'name': u'Serthis Potionmaster', 'id': u'6332'}, {'src': u'/images/cms/familiar/art/413.png', 'loyalty': u'Relaxed', 'name': u'Smoke Gyre', 'id': u'413'}, {'src': u'/images/cms/familiar/art/7697.png', 'loyalty': u'Relaxed', 'name': u'Snarling Mimic', 'id': u'7697'}, {'src': u'/images/cms/familiar/art/13423.png', 'loyalty': u'Relaxed', 'name': u'Stonewatch Prince', 'id': u'13423'}, {'src': u'/images/cms/familiar/art/343.png', 'loyalty': u'Relaxed', 'name': u'Trick of the Light', 'id': u'343'}, {'src': u'/images/cms/familiar/art/10227.png', 'loyalty': u'Relaxed', 'name': u'Ultramel Amphithere', 'id': u'10227'}, {'src': u'/images/cms/familiar/art/2259.png', 'loyalty': u'Relaxed', 'name': u'Umberhorn Qiriq', 'id': u'2259'}, {'src': u'/images/cms/familiar/art/13422.png', 'loyalty': u'Relaxed', 'name': u'Windcarve Fugitive', 'id': u'13422'}, {'src': u'/images/cms/familiar/art/6339.png', 'loyalty': u'Relaxed', 'name': u'Wintermane Spearman', 'id': u'6339'}, {'src': u'/images/cms/familiar/art/7427.png', 'loyalty': u'Relaxed', 'name': u'Woodland Turkey', 'id': u'7427'}, {'src': u'/images/cms/familiar/art/13435.png', 'loyalty': u'Relaxed', 'name': u'Almandine Sturgeon', 'id': u'13435'}, {'src': u'/images/cms/familiar/art/13421.png', 'loyalty': u'Relaxed', 'name': u'Maren Warlock', 'id': u'13421'}, {'src': u'/images/cms/familiar/art/1929.png', 'loyalty': u'Relaxed', 'name': u'Mistwatch Shellion', 'id': u'1929'}, {'src': u'/images/cms/familiar/art/6604.png', 'loyalty': u'Relaxed', 'name': u'Nephrite Chameleon', 'id': u'6604'}, {'src': u'/images/cms/familiar/art/905.png', 'loyalty': u'Relaxed', 'name': u'Nightsky Fuiran', 'id': u'905'}, {'src': u'/images/cms/familiar/art/1101.png', 'loyalty': u'Relaxed', 'name': u'Poultrygeist', 'id': u'1101'}, {'src': u'/images/cms/familiar/art/354.png', 'loyalty': u'Relaxed', 'name': u'Scarlet Flycatcher', 'id': u'354'}, {'src': u'/images/cms/familiar/art/1364.png', 'loyalty': u'Relaxed', 'name': u'Scythe Kamaitachi', 'id': u'1364'}, {'src': u'/images/cms/familiar/art/7597.png', 'loyalty': u'Relaxed', 'name': u'Sentinel Mith', 'id': u'7597'}, {'src': u'/images/cms/familiar/art/6332.png', 'loyalty': u'Relaxed', 'name': u'Serthis Potionmaster', 'id': u'6332'}, {'src': u'/images/cms/familiar/art/413.png', 'loyalty': u'Relaxed', 'name': u'Smoke Gyre', 'id': u'413'}, {'src': u'/images/cms/familiar/art/7697.png', 'loyalty': u'Relaxed', 'name': u'Snarling Mimic', 'id': u'7697'}, {'src': u'/images/cms/familiar/art/13423.png', 'loyalty': u'Relaxed', 'name': u'Stonewatch Prince', 'id': u'13423'}, {'src': u'/images/cms/familiar/art/343.png', 'loyalty': u'Relaxed', 'name': u'Trick of the Light', 'id': u'343'}, {'src': u'/images/cms/familiar/art/10227.png', 'loyalty': u'Relaxed', 'name': u'Ultramel Amphithere', 'id': u'10227'}, {'src': u'/images/cms/familiar/art/2259.png', 'loyalty': u'Relaxed', 'name': u'Umberhorn Qiriq', 'id': u'2259'}, {'src': u'/images/cms/familiar/art/13422.png', 'loyalty': u'Relaxed', 'name': u'Windcarve Fugitive', 'id': u'13422'}, {'src': u'/images/cms/familiar/art/6339.png', 'loyalty': u'Relaxed', 'name': u'Wintermane Spearman', 'id': u'6339'}, {'src': u'/images/cms/familiar/art/7427.png', 'loyalty': u'Relaxed', 'name': u'Woodland Turkey', 'id': u'7427'}]
 -- inquisitive: 76 - [{'src': u'/images/cms/familiar/art/13434.png', 'loyalty': u'Inquisitive', 'name': u'Amber Gulper', 'id': u'13434'}, {'src': u'/images/cms/familiar/art/13433.png', 'loyalty': u'Inquisitive', 'name': u'Apatite Fisher', 'id': u'13433'}, {'src': u'/images/cms/familiar/art/13432.png', 'loyalty': u'Inquisitive', 'name': u'Arctic Hippalectryon', 'id': u'13432'}, {'src': u'/images/cms/familiar/art/1149.png', 'loyalty': u'Inquisitive', 'name': u'Bamboo Phytocat', 'id': u'1149'}, {'src': u'/images/cms/familiar/art/10669.png', 'loyalty': u'Inquisitive', 'name': u'Blue Vein Pansy', 'id': u'10669'}, {'src': u'/images/cms/familiar/art/2781.png', 'loyalty': u'Inquisitive', 'name': u'Brush Dodo', 'id': u'2781'}, {'src': u'/images/cms/familiar/art/2394.png', 'loyalty': u'Inquisitive', 'name': u'Bumble', 'id': u'2394'}, {'src': u'/images/cms/familiar/art/2590.png', 'loyalty': u'Inquisitive', 'name': u'Cardinal Hippogriff', 'id': u'2590'}, {'src': u'/images/cms/familiar/art/6336.png', 'loyalty': u'Inquisitive', 'name': u'Centaur Archer', 'id': u'6336'}, {'src': u'/images/cms/familiar/art/11815.png', 'loyalty': u'Inquisitive', 'name': u'Chromefeather Lookout', 'id': u'11815'}, {'src': u'/images/cms/familiar/art/13436.png', 'loyalty': u'Inquisitive', 'name': u'Clearwater Oracle', 'id': u'13436'}, {'src': u'/images/cms/familiar/art/2393.png', 'loyalty': u'Inquisitive', 'name': u'Coral Carpenter', 'id': u'2393'}, {'src': u'/images/cms/familiar/art/631.png', 'loyalty': u'Inquisitive', 'name': u'Corpse Cleaner', 'id': u'631'}, {'src': u'/images/cms/familiar/art/13429.png', 'loyalty': u'Inquisitive', 'name': u'Crystalplate Stinger', 'id': u'13429'}, {'src': u'/images/cms/familiar/art/14122.png', 'loyalty': u'Inquisitive', 'name': u'Deadland Disciple', 'id': u'14122'}, {'src': u'/images/cms/familiar/art/10667.png', 'loyalty': u'Inquisitive', 'name': u'Deadwood Boar', 'id': u'10667'}, {'src': u'/images/cms/familiar/art/11679.png', 'loyalty': u'Inquisitive', 'name': u'Depin', 'id': u'11679'}, {'src': u'/images/cms/familiar/art/415.png', 'loyalty': u'Inquisitive', 'name': u'Dreameater', 'id': u'415'}, {'src': u'/images/cms/familiar/art/357.png', 'loyalty': u'Inquisitive', 'name': u'Dryad', 'id': u'357'}, {'src': u'/images/cms/familiar/art/7698.png', 'loyalty': u'Inquisitive', 'name': u'Ectoplasmime', 'id': u'7698'}, {'src': u'/images/cms/familiar/art/904.png', 'loyalty': u'Inquisitive', 'name': u'Fuiran', 'id': u'904'}, {'src': u'/images/cms/familiar/art/611.png', 'loyalty': u'Inquisitive', 'name': u'Gale Wolf', 'id': u'611'}, {'src': u'/images/cms/familiar/art/414.png', 'loyalty': u'Inquisitive', 'name': u'Greater Sandstrike', 'id': u'414'}, {'src': u'/images/cms/familiar/art/4881.png', 'loyalty': u'Inquisitive', 'name': u'Harvest Floracat', 'id': u'4881'}, {'src': u'/images/cms/familiar/art/13427.png', 'loyalty': u'Inquisitive', 'name': u'Hippalectryon', 'id': u'13427'}, {'src': u'/images/cms/familiar/art/650.png', 'loyalty': u'Inquisitive', 'name': u'Hydra Scorpion', 'id': u'650'}, {'src': u'/images/cms/familiar/art/7699.png', 'loyalty': u'Inquisitive', 'name': u'Jawlocker', 'id': u'7699'}, {'src': u'/images/cms/familiar/art/13085.png', 'loyalty': u'Inquisitive', 'name': u'Juvenile Starsweeper', 'id': u'13085'}, {'src': u'/images/cms/familiar/art/11669.png', 'loyalty': u'Inquisitive', 'name': u'King Parda', 'id': u'11669'}, {'src': u'/images/cms/familiar/art/13086.png', 'loyalty': u'Inquisitive', 'name': u'Lesser Wisp', 'id': u'13086'}, {'src': u'/images/cms/familiar/art/13426.png', 'loyalty': u'Inquisitive', 'name': u'Moonbeam Crayfish', 'id': u'13426'}, {'src': u'/images/cms/familiar/art/3643.png', 'loyalty': u'Inquisitive', 'name': u'Nature Sprite', 'id': u'3643'}, {'src': u'/images/cms/familiar/art/6338.png', 'loyalty': u'Inquisitive', 'name': u'Painted Centaur', 'id': u'6338'}, {'src': u'/images/cms/familiar/art/747.png', 'loyalty': u'Inquisitive', 'name': u'Ragamouse', 'id': u'747'}, {'src': u'/images/cms/familiar/art/13425.png', 'loyalty': u'Inquisitive', 'name': u'Rhodochrosite Crane', 'id': u'13425'}, {'src': u'/images/cms/familiar/art/7596.png', 'loyalty': u'Inquisitive', 'name': u'Scrapmetal Tracker', 'id': u'7596'}, {'src': u'/images/cms/familiar/art/12522.png', 'loyalty': u'Inquisitive', 'name': u'Searing Jackalope', 'id': u'12522'}, {'src': u'/images/cms/familiar/art/4880.png', 'loyalty': u'Inquisitive', 'name': u'Snowsquall Floracat', 'id': u'4880'}, {'src': u'/images/cms/familiar/art/13434.png', 'loyalty': u'Inquisitive', 'name': u'Amber Gulper', 'id': u'13434'}, {'src': u'/images/cms/familiar/art/13433.png', 'loyalty': u'Inquisitive', 'name': u'Apatite Fisher', 'id': u'13433'}, {'src': u'/images/cms/familiar/art/13432.png', 'loyalty': u'Inquisitive', 'name': u'Arctic Hippalectryon', 'id': u'13432'}, {'src': u'/images/cms/familiar/art/1149.png', 'loyalty': u'Inquisitive', 'name': u'Bamboo Phytocat', 'id': u'1149'}, {'src': u'/images/cms/familiar/art/10669.png', 'loyalty': u'Inquisitive', 'name': u'Blue Vein Pansy', 'id': u'10669'}, {'src': u'/images/cms/familiar/art/2781.png', 'loyalty': u'Inquisitive', 'name': u'Brush Dodo', 'id': u'2781'}, {'src': u'/images/cms/familiar/art/2394.png', 'loyalty': u'Inquisitive', 'name': u'Bumble', 'id': u'2394'}, {'src': u'/images/cms/familiar/art/2590.png', 'loyalty': u'Inquisitive', 'name': u'Cardinal Hippogriff', 'id': u'2590'}, {'src': u'/images/cms/familiar/art/6336.png', 'loyalty': u'Inquisitive', 'name': u'Centaur Archer', 'id': u'6336'}, {'src': u'/images/cms/familiar/art/11815.png', 'loyalty': u'Inquisitive', 'name': u'Chromefeather Lookout', 'id': u'11815'}, {'src': u'/images/cms/familiar/art/13436.png', 'loyalty': u'Inquisitive', 'name': u'Clearwater Oracle', 'id': u'13436'}, {'src': u'/images/cms/familiar/art/2393.png', 'loyalty': u'Inquisitive', 'name': u'Coral Carpenter', 'id': u'2393'}, {'src': u'/images/cms/familiar/art/631.png', 'loyalty': u'Inquisitive', 'name': u'Corpse Cleaner', 'id': u'631'}, {'src': u'/images/cms/familiar/art/13429.png', 'loyalty': u'Inquisitive', 'name': u'Crystalplate Stinger', 'id': u'13429'}, {'src': u'/images/cms/familiar/art/14122.png', 'loyalty': u'Inquisitive', 'name': u'Deadland Disciple', 'id': u'14122'}, {'src': u'/images/cms/familiar/art/10667.png', 'loyalty': u'Inquisitive', 'name': u'Deadwood Boar', 'id': u'10667'}, {'src': u'/images/cms/familiar/art/11679.png', 'loyalty': u'Inquisitive', 'name': u'Depin', 'id': u'11679'}, {'src': u'/images/cms/familiar/art/415.png', 'loyalty': u'Inquisitive', 'name': u'Dreameater', 'id': u'415'}, {'src': u'/images/cms/familiar/art/357.png', 'loyalty': u'Inquisitive', 'name': u'Dryad', 'id': u'357'}, {'src': u'/images/cms/familiar/art/7698.png', 'loyalty': u'Inquisitive', 'name': u'Ectoplasmime', 'id': u'7698'}, {'src': u'/images/cms/familiar/art/904.png', 'loyalty': u'Inquisitive', 'name': u'Fuiran', 'id': u'904'}, {'src': u'/images/cms/familiar/art/611.png', 'loyalty': u'Inquisitive', 'name': u'Gale Wolf', 'id': u'611'}, {'src': u'/images/cms/familiar/art/414.png', 'loyalty': u'Inquisitive', 'name': u'Greater Sandstrike', 'id': u'414'}, {'src': u'/images/cms/familiar/art/4881.png', 'loyalty': u'Inquisitive', 'name': u'Harvest Floracat', 'id': u'4881'}, {'src': u'/images/cms/familiar/art/13427.png', 'loyalty': u'Inquisitive', 'name': u'Hippalectryon', 'id': u'13427'}, {'src': u'/images/cms/familiar/art/650.png', 'loyalty': u'Inquisitive', 'name': u'Hydra Scorpion', 'id': u'650'}, {'src': u'/images/cms/familiar/art/7699.png', 'loyalty': u'Inquisitive', 'name': u'Jawlocker', 'id': u'7699'}, {'src': u'/images/cms/familiar/art/13085.png', 'loyalty': u'Inquisitive', 'name': u'Juvenile Starsweeper', 'id': u'13085'}, {'src': u'/images/cms/familiar/art/11669.png', 'loyalty': u'Inquisitive', 'name': u'King Parda', 'id': u'11669'}, {'src': u'/images/cms/familiar/art/13086.png', 'loyalty': u'Inquisitive', 'name': u'Lesser Wisp', 'id': u'13086'}, {'src': u'/images/cms/familiar/art/13426.png', 'loyalty': u'Inquisitive', 'name': u'Moonbeam Crayfish', 'id': u'13426'}, {'src': u'/images/cms/familiar/art/3643.png', 'loyalty': u'Inquisitive', 'name': u'Nature Sprite', 'id': u'3643'}, {'src': u'/images/cms/familiar/art/6338.png', 'loyalty': u'Inquisitive', 'name': u'Painted Centaur', 'id': u'6338'}, {'src': u'/images/cms/familiar/art/747.png', 'loyalty': u'Inquisitive', 'name': u'Ragamouse', 'id': u'747'}, {'src': u'/images/cms/familiar/art/13425.png', 'loyalty': u'Inquisitive', 'name': u'Rhodochrosite Crane', 'id': u'13425'}, {'src': u'/images/cms/familiar/art/7596.png', 'loyalty': u'Inquisitive', 'name': u'Scrapmetal Tracker', 'id': u'7596'}, {'src': u'/images/cms/familiar/art/12522.png', 'loyalty': u'Inquisitive', 'name': u'Searing Jackalope', 'id': u'12522'}, {'src': u'/images/cms/familiar/art/4880.png', 'loyalty': u'Inquisitive', 'name': u'Snowsquall Floracat', 'id': u'4880'}]
 -- companion: 14 - [{'src': u'/images/cms/familiar/art/13431.png', 'loyalty': u'Companion', 'name': u'Chalcedony Snipper', 'id': u'13431'}, {'src': u'/images/cms/familiar/art/6605.png', 'loyalty': u'Companion', 'name': u'Corundum Chameleon', 'id': u'6605'}, {'src': u'/images/cms/familiar/art/12523.png', 'loyalty': u'Companion', 'name': u'Extinguished Jackalope', 'id': u'12523'}, {'src': u'/images/cms/familiar/art/2258.png', 'loyalty': u'Companion', 'name': u'Fungalhoof Qiriq', 'id': u'2258'}, {'src': u'/images/cms/familiar/art/359.png', 'loyalty': u'Companion', 'name': u'Shattered Serpent', 'id': u'359'}, {'src': u'/images/cms/familiar/art/13424.png', 'loyalty': u'Companion', 'name': u'Sparkling Stinger', 'id': u'13424'}, {'src': u'/images/cms/familiar/art/7598.png', 'loyalty': u'Companion', 'name': u'Spellbound Golem', 'id': u'7598'}, {'src': u'/images/cms/familiar/art/13431.png', 'loyalty': u'Companion', 'name': u'Chalcedony Snipper', 'id': u'13431'}, {'src': u'/images/cms/familiar/art/6605.png', 'loyalty': u'Companion', 'name': u'Corundum Chameleon', 'id': u'6605'}, {'src': u'/images/cms/familiar/art/12523.png', 'loyalty': u'Companion', 'name': u'Extinguished Jackalope', 'id': u'12523'}, {'src': u'/images/cms/familiar/art/2258.png', 'loyalty': u'Companion', 'name': u'Fungalhoof Qiriq', 'id': u'2258'}, {'src': u'/images/cms/familiar/art/359.png', 'loyalty': u'Companion', 'name': u'Shattered Serpent', 'id': u'359'}, {'src': u'/images/cms/familiar/art/13424.png', 'loyalty': u'Companion', 'name': u'Sparkling Stinger', 'id': u'13424'}, {'src': u'/images/cms/familiar/art/7598.png', 'loyalty': u'Companion', 'name': u'Spellbound Golem', 'id': u'7598'}]
 -- loyal: 10 - [{'src': u'/images/cms/familiar/art/11148.png', 'loyalty': u'Loyal', 'name': u'Mantled Foo', 'id': u'11148'}, {'src': u'/images/cms/familiar/art/412.png', 'loyalty': u'Loyal', 'name': u'Rainbow Sprite', 'id': u'412'}, {'src': u'/images/cms/familiar/art/13241.png', 'loyalty': u'Loyal', 'name': u'Stardust Scholar', 'id': u'13241'}, {'src': u'/images/cms/familiar/art/11147.png', 'loyalty': u'Loyal', 'name': u'Tigerblood Foo', 'id': u'11147'}, {'src': u'/images/cms/familiar/art/10226.png', 'loyalty': u'Loyal', 'name': u'Zalis', 'id': u'10226'}, {'src': u'/images/cms/familiar/art/11148.png', 'loyalty': u'Loyal', 'name': u'Mantled Foo', 'id': u'11148'}, {'src': u'/images/cms/familiar/art/412.png', 'loyalty': u'Loyal', 'name': u'Rainbow Sprite', 'id': u'412'}, {'src': u'/images/cms/familiar/art/13241.png', 'loyalty': u'Loyal', 'name': u'Stardust Scholar', 'id': u'13241'}, {'src': u'/images/cms/familiar/art/11147.png', 'loyalty': u'Loyal', 'name': u'Tigerblood Foo', 'id': u'11147'}, {'src': u'/images/cms/familiar/art/10226.png', 'loyalty': u'Loyal', 'name': u'Zalis', 'id': u'10226'}]
total = 682

"""

PRINT_TAMING_BESTIARY_PAGE__1_TO_3 = """locked: 6 - [{'src': u'/images/cms/familiar/art/16261_gray.png', 'loyalty': u'Locked', 'id': u'16261', 'name': u'Acid-Tongue Serpenta'}, {'src': u'/images/cms/familiar/art/16489_gray.png', 'loyalty': u'Locked', 'id': u'16489', 'name': u'Aer Phantom'}, {'src': u'/images/cms/familiar/art/16249_gray.png', 'loyalty': u'Locked', 'id': u'16249', 'name': u'Amethyst King'}, {'src': u'/images/cms/familiar/art/1779_gray.png', 'loyalty': u'Locked', 'id': u'1779', 'name': u'Arcane Sprite'}, {'src': u'/images/cms/familiar/art/14289_gray.png', 'loyalty': u'Locked', 'id': u'14289', 'name': u'Autumn Sea Dragon'}, {'src': u'/images/cms/familiar/art/16254_gray.png', 'loyalty': u'Locked', 'id': u'16254', 'name': u'Barking Jester'}]
awakened: 13
taming: 5
 -- wary: 1 - [{'src': u'/images/cms/familiar/art/16244.png', 'loyalty': u'Wary', 'id': u'16244', 'name': u'Bearded Yeti'}]
 -- tolerant: 1 - [{'src': u'/images/cms/familiar/art/12739.png', 'loyalty': u'Tolerant', 'id': u'12739', 'name': u'Amberwing Waveskimmer'}]
 -- relaxed: 0 - []
 -- inquisitive: 0 - []
 -- companion: 3 - [{'src': u'/images/cms/familiar/art/15298.png', 'loyalty': u'Companion', 'id': u'15298', 'name': u'Agol'}, {'src': u'/images/cms/familiar/art/15280.png', 'loyalty': u'Companion', 'id': u'15280', 'name': u'Animated Statue'}, {'src': u'/images/cms/familiar/art/12194.png', 'loyalty': u'Companion', 'id': u'12194', 'name': u'Anomalous Skink'}]
 -- loyal: 0 - []
total = 24

"""