$(function() {
    //if (!game_open) alert(game_close_txt);

//$('.flag01_input').mask('999,999,999,999');
//$('.flag02_input').mask('999,999,999,999');

    function real_sadari_loader() {
        top.location.reload();
    }
    setTimeout(refresh_sadari, ladder_refresh_time);

    function refresh_sadari() {
        real_sadari_loader();
    }
    $('#banner_ladder_open, #banner_ladder_close').click(function() {
        var bid = $(this).attr('id');
        if (bid == 'banner_ladder_open') {
            $('.banner_sadari').hide();
            $('.banner_sadari_detail').show();
        } else {
            $('.banner_sadari').show();
            $('.banner_sadari_detail').hide();
        }
    });
    $('#calc_type').tabify();
    $('.btn_typeA').click(function() {
        $('#clac_type').val('A');
			$('#TypeA').hide();
            $('#TypeB').show();
    });
    $('.btn_typeB').click(function() {
        $('#clac_type').val('B');
			$('#TypeB').hide();
            $('#TypeA').show();
    });
    $('.btn_partten_layout').click(function() {
        if ($(this).hasClass('active')) {
            $('.pic_close').removeClass('pic_close').addClass('pic_active');
            $(this).addClass('btn_pic_close').removeClass('btn_pic_active').removeClass('active');
        } else {
            $('.pic_active').removeClass('pic_active').addClass('pic_close');
            $(this).addClass('active').addClass('btn_pic_active').removeClass('btn_pic_close');
        }
        $('#partten_layout').toggle();
        $('#Type_picA div').scrollLeft(100000);
        $('#Type_picB div').scrollLeft(100000);
        $('#Type_picC div').scrollLeft(100000);
    });
    if (is_partten_fix) {
        $('#partten_layout').show();
    }
    if (bet_type == 'mixed') {
        $('#btn_more_layout').trigger('click');
    }
    if (coupon_event == 0) {
        $('#coupon_counter').countdown({
            image: IMG_DIR + '/clock/digits.png',
            startTime: cl_date,
            timerEnd: function() {
                $('#timerEnd_span').html('★★★ 사다리머니 충전시 보너스 쿠폰이 지급됩니다 ★★★');
            }
        });
    }
    $('#page_reload').click(function() {
        real_sadari_loader();
    });
    $('#bnt_money_refresh').click(function() {
			location.reload();
//        $.post(rt_path + '/_trans/member/get_money', {
//            mb_id: ladder_user_id
//        }, function(data) {
//            $('#gmoney').val(data.gmoney);
//            $('#my_point').html($.number(data.gpoint) + '원');
//            $('#calc_reset').trigger('click');
//            $('#games_rate, #games_rate1, #div_wingmoney').html('');
//        }, 'json');
    });
    $('#open_sdrguide').click(function() {
        //win_open('guide/sadari', 'SadariGuide', 'left=70,top=70,width=800,height=600,scrollbars=1,scroll=no');
    });
    $('.open_recommend').click(function() {
        //win_open('member/myrecom.asp', 'RecommendWindow', 'left=70,top=70,width=320,height=600,scrollbars=no,scroll=no');
    });
    $('#btn_partten_fix').click(function() {
        var chk = ($(this).is(':checked')) ? 1 : 0;
        $.post(rt_path + '/_trans/game/partten_fix', {
            pfix: chk
        });
    });
    $('#bet_allcheck').click(function() {
        if ($(this).is(':checked')) {
            $('.betting_chk1').prop('checked', true);
        } else {
            $('.betting_chk1').prop('checked', false);
        }
    });
    $('.s_games').on('click', function() {
        $('.s_games').removeClass('selected');
        $(this).toggleClass('selected');
    });
    $('.non_betting_submit').on('click', function() {
        alert('A non-gambling games.');
    });
    $('.betting_submit').on('click', function(e) {
        if (!game_open) {
            alert(game_close_txt);
            return false;
        }
        var sadari_min = parseInt($('#sadari_min').val());
        //var sadari_max = parseInt($(this).attr('bmax'));
		var sadari_max = parseInt($('#sadari_max').val());
        var cur_gmoney = parseInt($('#gmoney').val());
        var txt_game = Array('','BLUE', 'RED', '3LINE', '4LINE', 'LEFT', 'RIGHT', '3LINE+LEFT', '4LINE+LEFT', '3LINE+RIGHT', '4LINE+RIGHT', '4게임 논타이', '좌출발', '우출발', '3줄', '4줄', '좌3짝', '좌4홀', '우3홀', '우4짝');
        var betting_money = parseInt($('#betting_money').val());
        var rate = $(this).attr('rate');
		var gidx = $(this).attr('gidx');
		


        $('#games_rate, #games_rate1').html('X ' + rate);
        if (betting_money > 0) $('#div_wingmoney').removeClass('none').html($.number(betting_money * rate) + ' ');
        var bdate = $(this).parent('div').attr('bdate');
        var atime = $(this).parent('div').attr('atime');
        $('#bet_date').val(bdate);
        $('#bet_atime').val(atime);
		$('#Benefit').val(rate);
		$('#IG_Idx').val(gidx);
        
		if (cur_gmoney < 100) {
            if (confirm('Money is not enough to hold bets. \n is in charge of this page you need money to go')) {
                parent.location.href = '/m/money/charge.asp';
            }
            return false;
        }
        if (sadari_min > 0 && betting_money < sadari_min) {
            alert('Minimum amount of bets' + $.number(sadari_min) + ' ');
			//refresh_sadari();
            return false;
        }
        if (sadari_max > 0 && betting_money > sadari_max) {
            alert('The maximum bet amount Restricted' + $.number(sadari_max) + ' ');
			refresh_sadari();
            return false;
        }
        var bet_date = bdate.split('-');
        var atime1 = (atime != 288) ? parseInt(atime) + 1 : 1;
        var atime2 = (atime1 != 288) ? parseInt(atime1) + 1 : 1;
        var atime3 = (atime2 != 288) ? parseInt(atime2) + 1 : 1;
        var game = $(this).attr('game');
		var betting = $(this).attr('betting');
		$('#ICT_BetNum').val(betting);
        if (game < 12) {
            if (game > 2) atime += ',' + atime1;
            if (game > 2 && game != 5 && game != 6) atime += ',' + atime2;
            if (game >= 10) atime += ',' + atime3;
        }
        var txt_atime = bet_date[1] + ' - ' + bet_date[2] + ' - ' + atime + ' # ';
        var txt_betting_money = $('#div_gmoney').text();
        if (betting_money == 0 || !$.isNumeric(betting_money)) {
            alert('Pour a can thank enter your betting money.');
            return false;
        }
        if (!confirm(txt_atime + ' [' + txt_game[game] + '] ' + txt_betting_money + 'Are you sure you want \n Click OK when you pour a grace.')) {
            $('#games_rate, #games_rate1, #div_wingmoney').html('');
            return false;
        }
        $('#betting').val(betting);
        parent.sadari_uiblock();
        $.post(rt_path + '/game/ladder/ladder.asp', $('#form_betting').serialize(), function(res) {
            var msg = res.msg.replace(/\\n/g, '\n');
            if (res.t == 1) {
                alert(msg);
            } else {
                if (res.msg) alert(msg);
            }
            location.reload();
            parent.sadari_uiunblock();
        }, 'json');
    });
    $(document).bind("contextmenu", function() {
        return false;
    });
    $(document).keydown(function(e) {
        var allowPageList = new Array();
        var bBlockF5Key = true;
        for (number in allowPageList) {
            var regExp = new RegExp('^' + allowPageList[number] + '.*', 'i');
            if (regExp.test(document.location.pathname)) {
                bBlockF5Key = false;
                break;
            }
        }
        if (bBlockF5Key) {
            if (e.which === 116) {
                if (typeof event == "object") {
                    event.keyCode = 0;
                }
                return false;
            } else if (e.which === 82 && e.ctrlKey) {
                return false;
            }
        }
    });
});
