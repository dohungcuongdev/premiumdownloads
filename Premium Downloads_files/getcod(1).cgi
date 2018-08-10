<!--
function _ssPre() { if ((typeof document.webkitVisibilityState!='undefined' && document.webkitVisibilityState=='prerender') || (typeof document.visibilityState!='undefined' && (document.visibilityState=='prerender' || document.visibilityState[0]=='prerender'))) return 1; return 0;}
function cCk(nm,vl,mn){var ex=cdm="";var _sscdom="";if (_ssPre()) { return; } if (_sscdom && _sscdom!="") { cdm=" domain="+_sscdom; if (mn) {document.cookie=nm+"=; expires=Thu, 01-Jan-70 00:00:01 GMT; path=/;";}}if (mn) {var d=new Date();d.setTime(d.getTime()+(mn*6*1000)); ex="; expires="+d.toGMTString();} document.cookie=nm+"="+vl+ex+"; path=/;"+cdm+"";}
function rCk(nm){var nEQ=nm+"=";if (_ssPre()) { return; } var ca=document.cookie.split(';');for(var i=0;i<ca.length;i++){var c=ca[i]; while(c.charAt(0)==' ') c=c.substring(1,c.length); if(c.indexOf(nEQ) == 0) return c.substring(nEQ.length,c.length);}return null;}
function ud(){var u=""+o_.getTime();return(u);}
function udtb(){var u=""+otb_.getTime();return(u);}
function _ssrit(m){var n=new Date();var eT=n.getTime()+m;while(true){n=new Date();if(n.getTime()>eT){return;}}}
function _ssvoid(){return;}
function _ssHash(k) { var h = 0, g;for (var i=0;i<k.length-1;i++) {h=(h<<4)+parseInt(k.charCodeAt(i));if (g=h&0xF0000000)h^=g>>24;h&=~g;}return(h);}
function ssxl(xl_,r){var i_=new Image(1,1);i_.src="https://s18.shinystat.com/cgi-bin/csa.cgi?USER="+usPOVSW_+"&"+xl_+"&RM="+Math.round(Math.random()*2147483647);if(r){_ssrit(r);}else{_ssrit(500);}i_.onload=function(){_ssvoid();}}
function sseXr(a,b){var rt="";for(var i=0;i<a.length;i++){rt+=String.fromCharCode(b^a.charCodeAt(i));}return(rt);}
function _sse(_o, e, f){if(window.addEventListener){ _o.addEventListener(e, f, false);}else if(window.attachEvent){ _o.attachEvent('on'+e, f);}else{}}
function _ttr(_t){cCk("TTR_"+usPOVSW_,_t);} // for js reload insert this function before location.reload 
function _cttr(){ if (_tr=rCk("TTR_"+usPOVSW_)){document.cookie = "TTR_"+usPOVSW_+"=; expires=Thu, 01-Jan-70 00:00:01 GMT; path=/;";return("&RFS="+_tr);}else return("");}
function _chkr(){var _mt=document.getElementsByTagName('meta');var _ttr="";var _tr=0;for(var i=0;i<_mt.length;i++) {var _cd=_mt[i].httpEquiv.toLowerCase();if(_cd.indexOf('refresh')>-1){_pp = _mt[i].content.indexOf(';');if (_pp>-1) {_ttr = _mt[i].content.substr(0,_pp+1);}else{_ttr = _mt[i].content;}}}_tr=parseInt(_ttr,10);if (_tr) { return (_tr); }else{return 0;}}
function _sstepPOVSW(e){var oe=new Date();var _dt=Math.round((oe.getTime()-tbro_)/1000);if (_tr=_chkr())if ((_dt>=(_tr-2)) && (_dt <=(_tr+2))) _ttr(_tr);cCk("SN_"+usPOVSW_,stfCkPOVSW(snPOVSW_,svPOVSW_,_dt),2592000);}
function sseC(d) {if (typeof(encodeURIComponent) == 'function') {return encodeURIComponent(d);} else {return escape(d);}}
function ssORDCK(){if (!okcvPOVSW_){ if (typeof(_ssCONV) !== 'undefined') { okcvPOVSW_=_ssCONV; return(_ssCONV);} return(""); } return(okcvPOVSW_);}
function ssORD(){var _par_="SSCONV="+ssORDCK();var argv = ssORD.arguments;if (_paguPOVSW.length>1) {_par_+="&"+_paguPOVSW}if (argv[0].length<=1) {_cidorPOVSW=""+o_.getDate()+o_.getMonth()+"-"+rssidPOVSW_;argv[0]=_cidorPOVSW;} else{ _cidorPOVSW=""+sseC(argv[0]);}for (var i = 0; i<argv.length && i<_cvt.length; i++) {if (argv[i]) _par_+="&"+_cvt[i]+sseC(argv[i]);}_sscAPOVSW[_idxcAPOVSW++] = _par_+pccPOVSW_+ssidPOVSW_;}
function ssORDnm() {var argv = ssORDnm.arguments;ssORD(argv[0], 0, 0, 0, argv[1], argv[2], argv[3]);}
function ssPROD(){ var _conv="SSCONV="+ssORDCK(); var _par_=_conv+"&"+_cvt[0]+_cidorPOVSW;var argv = ssPROD.arguments;for (var i = 0; i < argv.length && i<_cvp.length; i++) {if (argv[i]) _par_+="&"+_cvp[i]+sseC(argv[i]);}_par_+="&C_IXPR="+_idxcAPOVSW;_sscAPOVSW[_idxcAPOVSW++] = _par_;}
function ssPRODnm() {var argv = ssPRODnm.arguments;ssPROD(argv[0], argv[1], 0, argv[2], argv[3]);}
function ssCvTrack(){ function ssaRls(nm){ try { if (localStorage.getItem(nm)==null) {if (sessionStorage.getItem(nm)==null) {return 0};return(sessionStorage.getItem(nm)); }else{return(localStorage.getItem(nm));}}catch(e_r){}};var _sscmp="";var _ssa="";_sscmp=rCk("SSIDC_"+usPOVSW_);_ssa=ssaRls("SSA");for (var i = 0; i < _sscAPOVSW.length; i++) { if (_sscAPOVSW[i].indexOf("C_PRTO")>-1) { _sscAPOVSW[i]+="&C_NUPR="+(_sscAPOVSW.length-1); if (_sscmp) _sscAPOVSW[i]+="&CAMP="+_sscmp; } if (_ssa) _sscAPOVSW[i]+="&SSA="+_ssa; ssxlPOVSW(_sscAPOVSW[i]);}}
function scCk(cck,v,r){var ca=_fr_=_ioi_=_id_=_tuv_=_fhr_=_lhr_=_hr_="";var _lr_=r;var _v_=_p_=_pvc_=idx=1;var _tfr_=_tuv_=ud();if (!v) v=0;_hr_=_vhrPOVSW;if (self != top){try {_hr_=document.referrer;}catch(e_r){}}_lhr_=sseC(_hr_);if ((idx=_lr_.indexOf(document.domain))>0) {if (idx<9) _lr_="";}idx=_hr_.indexOf('?');if (idx>-1) _lhr_=sseC(_hr_.substr(idx));if (okcvPOVSW_) {_id_=rssidPOVSW_;}if (cck) {ca = cck.split('%G');_v_=parseInt(ca[0],10);if (!isNaN(ca[6])) {_pvc_=parseInt(ca[6],10)+1;}_p_=parseInt(ca[1],10)+1;if (!(parseInt(ca[7],10))) _tuv_=ud();else _tuv_=ca[7];if (otb_.getTime()-parseInt(v,10)>st_) {_v_++;_pvc_=1;_tuv_=o_.getTime();} _fr_=ca[2];_fhr_=ca[8];_tfr_=ca[3];if (!_lr_) _lr_=ca[4]; if (!_lhr_) _lhr_=ca[9];if (!ca[5]) ca[5]=_id_;  else _id_=ca[5];}else{_fr_=_lr_;_fhr_=_lhr_;}_lhr_="";_lr_="";_ioi_=""+_v_+"%G"+_p_+"%G"+_fr_+"%G"+_tfr_+"%G"+_lr_+"%G"+_id_+"%G"+_pvc_+"%G"+_tuv_+"%G"+_fhr_+"%G"+_lhr_; pccPOVSW_="&"+_cve[0]+_v_+"&"+_cve[1]+_p_+"&"+_cve[2]+_fr_+"&"+_cve[3]+_tfr_+"&"+_cve[4]+_lr_+"&"+_cve[5]+_id_+"&"+_cve[6]+_pvc_+"&"+_cve[7]+_tuv_;pccPOVSW_+="&"+_cve[8]+_lhr_+"&"+_cve[9]+_fhr_;return(_ioi_);}
function sswk_(tnow){var w = Math.floor( ( (tnow / 86400000 ) - 4) / 7);return w}
function stfCkPOVSW(ck,v,upt){var ca=_pt_=_iof_=can="";var _f_=uv_=uvw=1;var _tf_=ud();var _t_=_bu_=0;_ort=new Date();_ort.setTime(o_.getTime()+(1000*ssoffset_));if (!v) v=0;if (ck) {ca = ck.split('%G');_f_=parseInt(ca[2],10);_tf_=parseInt(ca[3],10);if (o_.getTime()-parseInt(v,10)>st_){_ot=new Date();_ot.setTime(parseInt(_tf_,10)+(1000*ssoffset_)); if(_ort.getUTCMonth()==_ot.getUTCMonth()){_f_++;}else{_f_=1;_tf_=ud();}}_t_=ca[0];_pt_=ca[1];_bu_=ca[4];if (ca[5]) can=ca[5];}if (upt) {if (_paguPOVSW.length>1) {_pt_=_paguPOVSW.substring(4);}else{_pt_=""+sseC(window.location.href);} _t_=upt;}_ot=new Date();_ot.setTime(parseInt(_bu_,10)+(1000*ssoffset_));if ((_ort.getUTCDay()==_ot.getUTCDay())&&(_ort.getUTCMonth()==_ot.getUTCMonth())&&(_ort.getUTCFullYear()==_ot.getUTCFullYear())) uv_=0;if (sswk_(_ort) == sswk_(_ot)) uvw=0;_iof_=""+_t_+"%G"+_pt_+"%G"+_f_+"%G"+_tf_+"%G"+ud()+"%G"+SScanPOVSW(1);tfPOVSW_="&TUP="+_t_+"&PTUP="+_pt_+"&FV="+_f_+"&UV="+uv_+"&US="+uvw+"&DUP="+(_bu_/1000)+"&PCNL="+can;return(_iof_);}
function _sslinkd(_uj,nodl){var pc,sqs,shr,a,b,c,d,h,exl;var sdl=document.location;if (!_uj || _uj=="") return;sqs = _uj.indexOf("?"); shr = _uj.indexOf("#"); a=rCk("SSC_"+usPOVSW_);b=rCk("SV_"+usPOVSW_,1);c=rCk("SN_"+usPOVSW_);h=a+b+c;d=_ssHash(h.toUpperCase());pc ="SSC__="+a+"&SV__="+b+"&SN__="+c+"&SHS__="+d;if (pc) {if (sqs==-1 && shr==-1) exl=_uj+"?"+pc;else if (shr==-1) exl=_uj+"&"+pc;else if (sqs==-1) exl=_uj.substring(0,shr-1)+"?"+pc+_uj.substring(shr);else exl=_uj.substring(0,shr-1)+"&"+pc+_uj.substring(shr);if (nodl) {return(exl);}else{ sdl.href=exl;}}else { if (nodl) {return(_uj);}else{ sdl.href=_uj;}}}
function _sspostd(_fj){var pc,sqs,shr,a,b,c,d,h;if (!_fj || !_fj.action) return;sqs = _fj.action.indexOf("?"); shr = _fj.action.indexOf("#"); a=rCk("SSC_"+usPOVSW_);b=rCk("SV_"+usPOVSW_);c=rCk("SN_"+usPOVSW_);h=a+b+c;d=_ssHash(h.toUpperCase());pc ="SSC__="+a+"&SV__="+b+"&SN__="+c+"&SHS__="+d;if (pc) {if (_fj.method = 'post') {var inp = document.createElement('input');inp.type = 'hidden';inp.name = '_sspostd';inp.value = pc;_fj.appendChild(inp);}else{if (sqs==-1 && shr==-1) _fj.action+="?"+pc;else if (shr==-1) _fj.action+="&"+pc;else if (sqs==-1) _fj.action=_fj.action.substring(0,shr-1)+"?"+pc+_fj.action.substring(shr);else _fj.action=_fj.action.substring(0,shr-1)+"&"+pc+_fj.action.substring(shr);}}return;}
function objQS(qs){ dic = new Array();if(!qs) qs = location.search.substring(1);if(qs!=""){aQs = qs.split('&');for(i=0;i<aQs.length;i++){aPV = aQs[i].split('=');dic[aPV[0]]=aPV[1];}}return dic}
function ckrld(){var dl=document.location;var qs=dla=a=b=c=d=e=h="";dla=dl.href.substring(dl.href.indexOf('#'));if (dla && dla!="") qs=dla+"&";qs+=dl.search.substring(1);if(qs && qs!="" && qs.indexOf("SV__=")>=0) {var pck=objQS(qs);if ( qs.indexOf("SSNP__=")>=0 ) {a=decodeURIComponent(pck['SSC__']);b=decodeURIComponent(pck['SV__']);c=decodeURIComponent(pck['SN__']);d=decodeURIComponent(pck['SHS__']);e=decodeURIComponent(pck['SSID__']);}else{a=pck['SSC__'];b=pck['SV__'];c=pck['SN__'];d=pck['SHS__'];e=pck['SSID__'];}h=a+b+c;if (_ssHash(h.toUpperCase()) != d) return;if (a && a!="") cCk("SSC_"+usPOVSW_,a,2592000);if (b && b!="") cCk("SV_"+usPOVSW_,b);if (e && e!="") cCk("SSID_"+usPOVSW_,e);if (c && c!="") cCk("SN_"+usPOVSW_,c,2592000);}}
function ssadbk(qs) { var img; img = new Image(); img.src = "//advm.brznetwork.com/commons/adsense.png"; img.onload = function() { return;}; img.onerror = function() { var iabk_=new Image(1,1); iabk_.src="https://s18.shinystat.com/cgi-bin/adbsa.cgi" + qs +"&RM="+Math.round(Math.random()*2147483647); iabk_.onload=function(){return;} }; }
function SSsdk(e){return("");} function SScanPOVSW(){return("");}var ssxlPOVSW=ssxl;var _cvt=new Array("C_IDOR=","C_PRTO=","C_PRTA=","C_PRSP=","C_NAZ=","C_PROV=","C_CITT=","C_USR0=","C_USR1=","C_USR2=","C_USR3=","C_USR4=","C_USR5=","C_USR6=","C_USR7=","C_USR8=","C_USR9=");var _cvp=new Array("C_IDPR=","C_QTA=","C_PRUN=","C_DEPR=","C_CATE=");
var _cidorPOVSW;usPOVSW_="TRO-juicets";n_=c_="";l_=""+screen.width;y_=""+screen.height;v_=navigator;d_=document.referrer;dh_=window.location.href;var o_=new Date();var otb_=new Date();vu_="&VUT=-1";
ebl_="cdgnsdtomn`e";_edbl=tfPOVSW_=pccPOVSW_=okcvPOVSW_=_paguPOVSW=_vhrPOVSW=svPOVSW_=snPOVSW_=ckadPOVSW="";
var _cve=new Array("C_VISI=","C_PVIS=","C_REFP=","C_DATP=","C_REF=","C_IDCO=","C_PVCO=","C_DATV=","C_PAG=","C_PAGP=");ssidPOVSW_="&SSID=";par_="&NODW=yes&PAG=https://imperivm-world.forumcommunity.net&RM=1790127487";
var _sscAPOVSW= new Array();var _idxcAPOVSW=0;
tbro_=o_.getTime();o_.setTime(1000*1533873933);var ssoffset_=7200;var rssidPOVSW_=Math.round(Math.random()*ud());var st_=1800000;var csp_=par_.split('&');
for(_i__=0;_i__<csp_.length;_i__++) {if (csp_[_i__].indexOf("PAG=")>-1) _paguPOVSW=csp_[_i__];if (csp_[_i__].indexOf("SSCONV=")>-1) okcvPOVSW_=csp_[_i__].substring(7,csp_[_i__].length);if (csp_[_i__].indexOf("CKAD=")>-1) ckrld();}_edbl=sseXr(ebl_,1);r_=""+sseC(d_);
if (self != top){try {r_=""+sseC(parent.document.referrer)+"&FHR="+sseC(d_);}catch(e_r){}}to_=ud();
k_="&CK="+(v_.cookieEnabled?"Y":"N");
j_="&JV="+(v_.javaEnabled()?"Y":"N");hr_="&HR="+sseC(dh_);fd_=dh_.indexOf("?ssidc=");
if (fd_>-1){cCk("SSIDC_"+usPOVSW_,dh_.substr(7+fd_,dh_.length),86400);}if(v_.appName!="Netscape"){c_=screen.colorDepth}else{c_=screen.pixelDepth}
if (svPOVSW_ = rCk("SV_"+usPOVSW_)){var det=otb_.getTime()-parseInt(svPOVSW_,10);vu_="&VUT="+det;if (det>st_) {cCk("SSID_"+usPOVSW_,rssidPOVSW_);ssidPOVSW_+=rssidPOVSW_;_vhrPOVSW=""+dh_;}else{ssidPOVSW_+=rCk("SSID_"+usPOVSW_);}}else {cCk("SSID_"+usPOVSW_,rssidPOVSW_);ssidPOVSW_+=rssidPOVSW_;_vhrPOVSW=""+dh_;}cCk("SV_"+usPOVSW_,udtb());
if (ssc_=rCk("SSC_"+usPOVSW_)){cCk("SSC_"+usPOVSW_,scCk(ssc_,svPOVSW_,r_),2592000);}else{cCk("SSC_"+usPOVSW_,scCk("",svPOVSW_,r_),2592000);}if (snPOVSW_=rCk("SN_"+usPOVSW_)){cCk("SN_"+usPOVSW_,stfCkPOVSW(snPOVSW_,svPOVSW_,""),2592000);}else{n_="&NUT=y";cCk("SN_"+usPOVSW_,stfCkPOVSW("",svPOVSW_,""),2592000);}
var ssqS_="https://s18.shinystat.com/cgi-bin/csa.cgi?USER="+usPOVSW_+par_+"&REFER="+r_+"&COLOR="+c_+"&SIZE="+l_+"&RES="+l_+"X"+y_+k_+hr_+j_+vu_+n_+ssidPOVSW_+tfPOVSW_+_cttr()+SSsdk(svPOVSW_)+SScanPOVSW()+"&JS=Y&VJS=4033CSA";
if (_ssPre()){ssqS_=ssqS_+"&PRRD=1"}
if (par_.indexOf("NODW=yes")>-1){var ig_=new Image(1,1);ig_.src=ssqS_+"&RM="+Math.round(Math.random()*2147483647);ig_.onload=function(){_ssvoid();}}
else{document.write("<a href=\"https://s18.shinystat.com/cgi-bin/shinystatv.cgi?USER="+usPOVSW_+"&NH=1\" Target=\"_new\"><img src=\""+ssqS_+"\" border=\"0\"/></a>"); }
ssadbk(ssqS_.substring(ssqS_.indexOf('?')));
if (window.sslinker) {(function(linkdata, linkdom){var linkdata = {};linkdata['SSNP__']=1;linkdata['SSID__']=rCk("SSID_"+usPOVSW_);linkdata['SSC__']=rCk("SSC_"+usPOVSW_);linkdata['SV__']=rCk("SV_"+usPOVSW_);linkdata['SN__']=rCk("SN_"+usPOVSW_);h=linkdata['SSC__']+linkdata['SV__']+linkdata['SN__'];linkdata['SHS__']=_ssHash(h.toUpperCase());var getLocation = function(href) {var l = document.createElement("a");l.href = href;return l;};var getUrlVars = function(href) {if (!href)return {};var vars = {}, hash;var hashes = href.slice(href.indexOf('?') + 1).split('&');for (var i = 0; i < hashes.length; i++) {hash = hashes[i].split('=');vars[hash[0]] = hash[1];} return vars;}; var serialize = function(obj) {var str = [];for(var p in obj)if (obj.hasOwnProperty(p)) {str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));}return str.join("&");}; var domains = linkdom.split(',');for (var d = 0; d < domains.length; d++) {domains[d] = domains[d].trim();}for (var i = 0; i < document.links.length; i++) {var href = document.links[i].href;for (var d = 0; d < domains.length; d++) {if (href.indexOf(domains[d]) > -1) {var l = getLocation(href);if (l.hostname.indexOf(domains[d]) > -1) {document.links[i].addEventListener('click', function(evt){var vars = getUrlVars(this.href.split('?')[1]);var new_data = {};for (var k in linkdata) {new_data[k] = linkdata[k];}for (var k in vars) {new_data[k] = vars[k];}var new_href = this.href.split('?')[0] + '?' + serialize(new_data);var a = getLocation(new_href);a.target = this.target;document.body.appendChild(a);a.click();document.body.removeChild(a);evt.preventDefault();});}}}}})(window.sslinkdata, window.sslinkdom);}
if(1) {
    function ssaE(d){if (typeof(encodeURIComponent) == 'function') {return encodeURIComponent(d);} else {return escape(d);}}
    function ssaCss(){
        var par="";
        try{
            if (typeof tfPOVSW_ != 'undefined') {par+=tfPOVSW_;}
            else{ if (typeof tf_ != 'undefined') {par+=tf_;}}             
            if (typeof par_ != 'undefined'){
              var psl=par_.split('&');
              for(var i=0;i<psl.length;i++) {
                  if (psl[i].indexOf("EMD5=")>-1) par+="&"+psl[i];
                  if (psl[i].indexOf("SEMER=")>-1) par+="&"+psl[i];
                  if (psl[i].indexOf("COCAM=")>-1) par+="&"+psl[i];
              }
            }
        }catch (e_r){}
        return (par);
    }
    function ssaCls(nm,vl){try{ sessionStorage.setItem(nm,vl);localStorage.setItem(nm,vl);}catch(e_r){}}
    function ssaRls(nm){ try { if (localStorage.getItem(nm)==null) {if (sessionStorage.getItem(nm)==null) {return 0};return(sessionStorage.getItem(nm)); }else{return(localStorage.getItem(nm));}}catch(e_r){}}
    function ssaPm (e) {
        if (e == null) return;
        var msg=e.data;
        if (typeof msg === 'string' || msg instanceof String){   
                if (msg.indexOf("ssa_ls")>-1) {
                        var ssa=msg.split('|');
                        if (ssa[1]){
                                if (ssa[1] != ssaRls("SSA")) { ssaCls("SSA",ssa[1]);}
                        }
                }
        }
    }
    function ssaif(){        
        var rf_=ssaE(document.referrer);
        if (self != top){try {rf_=""+ssaE(parent.document.referrer)}catch(e_r){}}
        var sls_=ssaRls("SSA");
        var nvs=0;
        if ((typeof vu_!="undefined") && vu_.indexOf("-1")>-1) {nvs=1;}
        else {if (parseInt(vu_.substring(1+vu_.indexOf("=")),10)>1800000 ) {nvs=1;}}               
        var ssals_="";
        if (sls_) {ssals_=sls_;}
        var uri="https://codicebusiness.shinystat.com/cgi-bin/getcod.cgi?IFSSA=yes&IDS=18294099&SSA="+ssals_+"&RF="+rf_+"&HR="+ssaE(window.location.href)+ssaCss()+"&NV="+nvs+"&RM="+Math.round(Math.random()*2147483647); 
        if (document.getElementById('ifssa')){
            //document.getElementById('ifssa').src=uri;
        }
        else{   
            try{                                                        
                ifssa = document.createElement("IFRAME"); 
                ifssa.setAttribute("src", uri); 
                ifssa.setAttribute("id", "ifssa"); 
                ifssa.setAttribute("name", "ifssa"+Math.round(Math.random()*100000)); 
                ifssa.setAttribute("tabindex", "-1");
                ifssa.setAttribute("sandbox", "allow-same-origin allow-scripts");
                ifssa.style.width = 0+"px"; 
                ifssa.style.height = 0+"px";    
                ifssa.style.display = "none";
                document.body.appendChild(ifssa);
                if (window.addEventListener) {window.addEventListener("message", ssaPm, false);}else {window.attachEvent("onmessage", ssaPm);}           
            }
            catch(e_r){}                                                         
        }
    }

    var infb="0";
    var infgen="0";
    if (infb!="0"){
        _ssckcb = function() {        
                ssaif();
        };
    }
    else {
       var nzgdpr = ["AT","BE","BG","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE","IT","LV","LT","LU","MT","NL","PL","PT","RO","SK","SI","ES","SE","GB"];
       var okgdpr=1;
       for(var i=0;i<nzgdpr.length;i++){ if (nzgdpr[i]=="RU") {okgdpr=0;break;}} 
       if (infgen!="0" || okgdpr){ssaif();}
    }

}

if (vu_.indexOf("-1")>-1) {
if (1) {
}
if (1){
    var _consentCallback = function(found) {
      var cmp="";
      if (found.length){
	      for (var i = 0; i < found.length; i++) { cmp+="$"+encodeURIComponent(found[i].name);}
      	      var dcmp_=new Image(1,1); 
              dcmp_.src="//s6.shinystat.com/cgi-bin/csa.cgi?USER=dcmp&PAG=18294099"+cmp+"&RM="+Math.round(Math.random()*2147483647);
              dcmp_.onload=function(){return;} 
      }
    };
    
    (function(cb) {
      var consentProviders = [];
      consentProviders.push({
        id: 1,
        name: 'iubenda',
        test: function() { return !!window._iub; }
      });
      consentProviders.push({
        id: 2,
        name: 'cookiebot',
        test: function() { return window.CookieConsent && window.Cookiebot; }
      });
      consentProviders.push({
        id: 3,
        name: 'generic CookieConsent-compliant (like cookiebot)',
        test: function() { return window.CookieConsent && !window.Cookiebot; }
      });
      consentProviders.push({
        id: 4,
        name: 'cookieconsent.insites.com',
        test: function() { return !!window.cookieconsent; }
      });
      consentProviders.push({
        id: 5,
        name: 'civicuk',
        test: function() { return window.CookieControl && !window.CookieConsent; }
      });
      consentProviders.push({
        id: 6,
        name: 'optanon by cookielaw.org',
        test: function() { return !!window.Optanon; }
      });
      consentProviders.push({
        id: 7,
        name: 'cookie-script.com',
        test: function() { return window.document.querySelectorAll('div[id^="cookiescript"]').length > 0; }
      });
      consentProviders.push({
        id: 8,
        name: 'generic cmp IAB guidelines compliant',
        test: function() { return !!window.__cmp; }
      });
      
      setTimeout(function() {
        var found = [];
        for (var i = 0; i < consentProviders.length; i++) {
          if (consentProviders[i].test()) {
            found.push({
              id: consentProviders[i].id,
              name: consentProviders[i].name
            });
          }
        }
        
        if (cb) {
          cb(found);
        }
      }, 1000);
    })(_consentCallback);
}

}
_sse(window, _edbl,_sstepPOVSW);
//-->
