var ratival, hl, straw, mypost;
var options = {};
loadLocalStorage();
createOptions();
createLink();


function loadLocalStorage() {		
	
	if (localStorage.getItem('hl') == null) {
		localStorage.setItem('hl', 'anypost');
	} else {
		JSON.parse(localStorage.getItem(hl));
	}
	
	checkLocalStorage('StrawPost', 0);
	checkLocalStorage('MyPost', 0);
	function checkLocalStorage(option, value) {
		if (localStorage.getItem(option) === null) {
			options[option] = value;
			localStorage.setItem(option, value)
		} else {
			options[option] = JSON.parse(localStorage.getItem(option));
		}
	}
}

var drationull = "любым рейтингом"
var dratio100 = "рейтингом выше 100"
var dratio500 = "рейтингом выше 500"
var dratio1000 = "рейтингом выше 1000"
var dratio3000 = "рейтингом выше 3000"

o = localStorage.getItem("ratival");
var clbk = document.querySelector('.value1');
var initClbk = new Powerange(
    clbk, {
    start: o,
    step: 1,
    min: 0,
    max: 4,
    hideRange: !0,
    callback: displayValue,
    }
);

function displayValue() {

	if (clbk.value == 0){
        clbk.value = drationull
        localStorage.setItem('ratival', 0);
    }
    if (clbk.value == 1){
        clbk.value = dratio100
        localStorage.setItem('ratival', 1); 
    }
    if (clbk.value == 2){
        clbk.value = dratio500
        localStorage.setItem('ratival', 2); 
    }
    if (clbk.value == 3){
        clbk.value = dratio1000
        localStorage.setItem('ratival', 3);
    }
    if (clbk.value == 4){
        clbk.value = dratio3000
        localStorage.setItem('ratival', 4);
    }
      document.getElementById('b-profile__value').innerHTML = clbk.value;
    }

function createOptions() {
	
	$('<h4 class="h4_border_yes" style="margin-top:25px">Настройки Pikabu Random</h4><table class="b-table" style="margin-bottom:40px"><tbody id="pikabuRandom"></tbody></table>').insertAfter($('[name="general"]'));

	var rndinj = '<tr><td>Показывать посты с <span class="b-profile__value" id="b-profile__value"></span></td><td style="width:150px"><input type="text" class="value1" /></td></tr>';
	$('#pikabuRandom').append(rndinj);
	
	
	var checkboxBgOff = {'border-color':'rgb(204, 206, 209)','box-shadow':'rgb(204, 206, 209) 0px 0px 0px 0px inset','transition':'border 0.4s, box-shadow 0.4s','-webkit-transition':'border 0.4s, box-shadow 0.4s','background-color':'rgb(204, 206, 209)'};
	var checkboxBgOn = {'border-color':'rgb(100, 189, 99)','box-shadow':'rgb(100, 189, 99) 0px 0px 0px 16px inset','transition':'border 0.4s, box-shadow 0.4s, background-color 1.2s','-webkit-transition':'border 0.4s, box-shadow 0.4s, background-color 1.2s','background-color':'rgb(100, 189, 99)'};
	var checkboxDotOff = {'left':'0px','transition':'left 0.2s','-webkit-transition':'left 0.2s','background-color':'rgb(255, 255, 255)'};
	var checkboxDotOn = {'left':'15px','transition':'left 0.2s','-webkit-transition':'left 0.2s','background-color':'rgb(255, 255, 255)'};
	
	
	createOption('MyPost', 'Показывать посты только с тегом МОЁ');
	createOption('StrawPost', 'Рандом по клубничке');
	
	$('.toolsCheckbox').parent().click(function() {
	    if ($(this).children('input').is(':checked')) {
	    	localStorage.setItem($(this).children('input').attr('id'), 0);
	    	$(this).children('input').prop('checked', 0);
			$(this).children('span').css(checkboxBgOff);
			$(this).find('small').css(checkboxDotOff);
	    } else {
	    	localStorage.setItem($(this).children('input').attr('id'), 1);
	    	$(this).children('input').prop('checked', 1);
			$(this).children('span').css(checkboxBgOn);
			$(this).find('small').css(checkboxDotOn);
	    }
	});

	function createOption(option, description) {
		var injection = '<tr><td><label for="'+option+'">'+description+'</label></td><td style="width:150px"><input id="'+option+'" name="'+option+'" type="checkbox" class="toolsCheckbox" value="1" style="display: none;" data-switchery="true"><span class="switchery"><small></small></span></td></tr>';
		$('#pikabuRandom').append(injection);
		if (options[option]) {
			$('#'+option).prop('checked', 1);
			$('#'+option+'+span').css(checkboxBgOn);
			$('#'+option+'+span>small').css(checkboxDotOn);
		} else {
			$('#'+option).prop('checked', 0);
			$('#'+option+'+span').css(checkboxBgOff);
			$('#'+option+'+span>small').css(checkboxDotOff);
		}
	}
	
}

function createLink(){

	if (localStorage.getItem("ratival")==0)
		localStorage.setItem('hl', 'anypost');
	if (localStorage.getItem("ratival")==1)
		localStorage.setItem('hl', 'hundred');
	if (localStorage.getItem("ratival")==2)
		localStorage.setItem('hl', 'fivehundred');
	if (localStorage.getItem("ratival")==3)
		localStorage.setItem('hl', 'thousand');
	if (localStorage.getItem("ratival")==4)
		localStorage.setItem('hl', 'threethousand');
	
		
	var getJSON = function(url, successHandler, errorHandler) {
		var xhr = typeof XMLHttpRequest != 'undefined'
				? new XMLHttpRequest()
				: new ActiveXObject('Microsoft.XMLHTTP');
			xhr.open('get', url, true);
			xhr.onreadystatechange = function() {
				var status;
				var data;
			// https://xhr.spec.whatwg.org/#dom-xmlhttprequest-readystate
			if (xhr.readyState == 4) { // `DONE`
				status = xhr.status;
				if (status == 200) {
					data = JSON.parse(xhr.responseText);
					successHandler && successHandler(data);
				} else {
					errorHandler && errorHandler(status);
				}
			}
		};
		xhr.send();
	};
	
	
	var ratio100 = localStorage.getItem("hl");
	var straw=localStorage.getItem("StrawPost");
	var mypost=localStorage.getItem("MyPost");
	
	
	var pkb = 'http://pikabu.ru/story/_'
	getJSON('http://pikabu.unnmd.ru/pikabu/' + ratio100 + '&pron=' +straw+ '&my=' +mypost+ '/', function(data) {
			var li = $('<li class="active menu-item-default"><a href="' + pkb + data.vratio + '" class="no_ch">Рандом</a></li>');
			li.appendTo($('[class="menu"]'));
	}, function(status) {
			alert('сервер Piakbu Random не доступен! =(\nМы скоро все поправим.');
	});

}

