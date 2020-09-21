var now = new Date();
var cookieTimeout = new Date(now.getFullYear() + 10, now.getMonth(), now.getDate());

var cookieLaw_disclaimer = "cookielaw_cscsviewer_accepted=true; expires=" + cookieTimeout.toUTCString();

function acceptDisclaimerCookie() {
    document.cookie = cookieLaw_disclaimer;
    document.body.removeChild(document.getElementById("cookieDisclaimer"));
}

function hasDisclaimerCookie() {
    return document.cookie.indexOf("cookielaw_cscsviewer_accepted=") > -1;
}

function checkCookieDisclaimer() {
    if (!hasDisclaimerCookie()) {
        var disclaimer = document.createElement("div");
        disclaimer.id = "cookieDisclaimer";
        disclaimer.innerHTML = '<table><tr><td width="*"><h6 style="color:#e06c00; font-weight: bold;">Cookies disclaimer</h6><p style="color:white">Our site saves small pieces of text information (cookies) on your device in order to deliver better content and for statistical purposes. You can disable the usage of cookies by changing the settings of your browser. By browsing these pages and using this tool without changing the browser settings you grant us permission to store that information on your device.</p>\n</td><td width="10%"><a id="cookieAgreeButton" class="btn btn-primary" onclick="javascript:acceptDisclaimerCookie();">Close</a></td></tr></table >';
        document.body.appendChild(disclaimer);
    }
}