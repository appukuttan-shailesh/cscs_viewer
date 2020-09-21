var cookieLaw_download = "cookielaw_ebrains_terms_accepted=true"

function acceptDownloadCookie() {
    document.cookie = cookieLaw_download;
}

function hasDownloadCookie() {
    return document.cookie.indexOf("cookielaw_ebrains_terms_accepted=") > -1;
}