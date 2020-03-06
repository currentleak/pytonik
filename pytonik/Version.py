###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import sys

VERSION = (1, 9, 8, 'alpha', 2)

if VERSION[3] and VERSION[4]:
    VERSION_TEXT = '{0}.{1}.{2}{3}{4}'.format(*VERSION)
else:
    VERSION_TEXT = '{0}.{1}.{2}'.format(*VERSION[0:3])

VERSION_EXTRA = ''
LICENSE = 'GPL3'
EDITION = ''  # Added in package names, after the version
KEYWORDS = "mvc, oop, module, python, framework, web, app"

PYVERSION_MA = sys.version_info.major
PYVERSION_MI = sys.version_info.minor

AUTHOR = "Pytonik"
ORG = "Betacodings"

MIME_TYPES = [
    {'ext': '.ai', 'type': 'application/postscript', 'mode': 'rb'},
    {'ext': '.aif', 'type': 'audio/x-aiff', 'mode': 'rb'},
    {'ext': '.aifc', 'type': 'audio/x-aiff', 'mode': 'rb'},
    {'ext': '.aiff', 'type': 'audio/x-aiff', 'mode': 'rb'},
    {'ext': '.asc', 'type': 'text/plain', 'mode': 'r'},
    {'ext': '.atom', 'type': 'application/atom+xml', 'mode': 'rb'},
    {'ext': '.au', 'type': 'audio/basic', 'mode': 'rb'},
    {'ext': '.avi', 'type': 'video/x-msvideo', 'mode': 'rb'},
    {'ext': '.bcpio', 'type': 'application/x-bcpio', 'mode': 'rb'},
    {'ext': '.bin', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.bmp', 'type': 'image/bmp', 'mode': 'rb'},
    {'ext': '.cdf', 'type': 'application/x-netcdf', 'mode': 'rb'},
    {'ext': '.cgm', 'type': 'image/cgm', 'mode': 'rb'},
    {'ext': '.class', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.cpio', 'type': 'application/x-cpio', 'mode': 'rb'},
    {'ext': '.cpt', 'type': 'application/mac-compactpro', 'mode': 'rb'},
    {'ext': '.csh', 'type': 'application/x-csh', 'mode': 'rb'},
    {'ext': '.css', 'type': 'text/css', 'mode': 'r'},
    {'ext': '.dcr', 'type': 'application/x-director', 'mode': 'rb'},
    {'ext': '.dif', 'type': 'video/x-dv', 'mode': 'rb'},
    {'ext': '.dir', 'type': 'application/x-director', 'mode': 'rb'},
    {'ext': '.djv', 'type': 'image/vnd.djvu', 'mode': 'rb'},
    {'ext': '.djvu', 'type': 'image/vnd.djvu', 'mode': 'rb'},
    {'ext': '.dll', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.dmg', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.dms', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.doc', 'type': 'application/msword', 'mode': 'rb'},
    {'ext': '.dtd', 'type': 'application/xml-dtd', 'mode': 'rb'},
    {'ext': '.dv', 'type': 'video/x-dv', 'mode': 'rb'},
    {'ext': '.dvi', 'type': 'application/x-dvi', 'mode': 'rb'},
    {'ext': '.dxr', 'type': 'application/x-director', 'mode': 'rb'},
    {'ext': '.eps', 'type': 'application/postscript', 'mode': 'rb'},
    {'ext': '.etx', 'type': 'text/x-setext', 'mode': 'r'},
    {'ext': '.exe', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.ez', 'type': 'application/andrew-inset', 'mode': 'rb'},
    {'ext': '.gif', 'type': 'image/gif', 'mode': 'rb'},
    {'ext': '.gram', 'type': 'application/srgs', 'mode': 'rb'},
    {'ext': '.grxml', 'type': 'application/srgs+xml', 'mode': 'rb'},
    {'ext': '.gtar', 'type': 'application/x-gtar', 'mode': 'rb'},
    {'ext': '.hdf', 'type': 'application/x-hdf', 'mode': 'rb'},
    {'ext': '.hqx', 'type': 'application/mac-binhex40', 'mode': 'rb'},
    {'ext': '.htm', 'type': 'text/html', 'mode': 'r'},
    {'ext': '.html', 'type': 'text/html', 'mode': 'r'},
    {'ext': '.ice', 'type': 'x-conference/x-cooltalk', 'mode': 'rb'},
    {'ext': '.ico', 'type': 'image/x-icon', 'mode': 'rb'},
    {'ext': '.ics', 'type': 'text/calendar', 'mode': 'r'},
    {'ext': '.ief', 'type': 'image/ief', 'mode': 'rb'},
    {'ext': '.ifb', 'type': 'text/calendar', 'mode': 'r'},
    {'ext': '.iges', 'type': 'model/iges', 'mode': 'rb'},
    {'ext': '.igs', 'type': 'model/iges', 'mode': 'rb'},
    {'ext': '.jnlp', 'type': 'application/x-java-jnlp-file', 'mode': 'rb'},
    {'ext': '.jp2', 'type': 'image/jp2', 'mode': 'rb'},
    {'ext': '.jpe', 'type': 'image/jpeg', 'mode': 'rb'},
    {'ext': '.jpeg', 'type': 'image/jpeg', 'mode': 'rb'},
    {'ext': '.jpg', 'type': 'image/jpeg', 'mode': 'rb'},
    {'ext': '.kar', 'type': 'audio/midi', 'mode': 'rb'},
    {'ext': '.latex', 'type': 'application/x-latex', 'mode': 'rb'},
    {'ext': '.lha', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.lzh', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.m3u', 'type': 'audio/x-mpegurl', 'mode': 'rb'},
    {'ext': '.m4a', 'type': 'audio/mp4a-latm', 'mode': 'rb'},
    {'ext': '.m4b', 'type': 'audio/mp4a-latm', 'mode': 'rb'},
    {'ext': '.m4p', 'type': 'audio/mp4a-latm', 'mode': 'rb'},
    {'ext': '.m4u', 'type': 'video/vnd.mpegurl', 'mode': 'rb'},
    {'ext': '.m4v', 'type': 'video/x-m4v', 'mode': 'rb'},
    {'ext': '.mac', 'type': 'image/x-macpaint', 'mode': 'rb'},
    {'ext': '.man', 'type': 'application/x-troff-man', 'mode': 'rb'},
    {'ext': '.mathml', 'type': 'application/mathml+xml', 'mode': 'rb'},
    {'ext': '.me', 'type': 'application/x-troff-me', 'mode': 'rb'},
    {'ext': '.mesh', 'type': 'model/mesh', 'mode': 'rb'},
    {'ext': '.mid', 'type': 'audio/midi', 'mode': 'rb'},
    {'ext': '.midi', 'type': 'audio/midi', 'mode': 'rb'},
    {'ext': '.mif', 'type': 'application/vnd.mif', 'mode': 'rb'},
    {'ext': '.mov', 'type': 'video/quicktime', 'mode': 'rb'},
    {'ext': '.movie', 'type': 'video/x-sgi-movie', 'mode': 'rb'},
    {'ext': '.mp2', 'type': 'audio/mpeg', 'mode': 'rb'},
    {'ext': '.mp3', 'type': 'audio/mpeg', 'mode': 'rb'},
    {'ext': '.mp4', 'type': 'video/mp4', 'mode': 'rb'},
    {'ext': '.mpe', 'type': 'video/mpeg', 'mode': 'rb'},
    {'ext': '.mpeg', 'type': 'video/mpeg', 'mode': 'rb'},
    {'ext': '.mpg', 'type': 'video/mpeg', 'mode': 'rb'},
    {'ext': '.mpga', 'type': 'audio/mpeg', 'mode': 'rb'},
    {'ext': '.ms', 'type': 'application/x-troff-ms', 'mode': 'rb'},
    {'ext': '.msh', 'type': 'model/mesh', 'mode': 'rb'},
    {'ext': '.mxu', 'type': 'video/vnd.mpegurl', 'mode': 'rb'},
    {'ext': '.nc', 'type': 'application/x-netcdf', 'mode': 'rb'},
    {'ext': '.oda', 'type': 'application/oda', 'mode': 'rb'},
    {'ext': '.ogg', 'type': 'application/ogg', 'mode': 'rb'},
    {'ext': '.pbm', 'type': 'image/x-portable-bitmap', 'mode': 'rb'},
    {'ext': '.pct', 'type': 'image/pict', 'mode': 'rb'},
    {'ext': '.pdb', 'type': 'chemical/x-pdb', 'mode': 'rb'},
    {'ext': '.pdf', 'type': 'application/pdf', 'mode': 'rb'},
    {'ext': '.pgm', 'type': 'image/x-portable-graymap', 'mode': 'rb'},
    {'ext': '.pgn', 'type': 'application/x-chess-pgn', 'mode': 'rb'},
    {'ext': '.pic', 'type': 'image/pict', 'mode': 'rb'},
    {'ext': '.pict', 'type': 'image/pict', 'mode': 'rb'},
    {'ext': '.png', 'type': 'image/png', 'mode': 'rb'},
    {'ext': '.pnm', 'type': 'image/x-portable-anymap', 'mode': 'rb'},
    {'ext': '.pnt', 'type': 'image/x-macpaint', 'mode': 'rb'},
    {'ext': '.pntg', 'type': 'image/x-macpaint', 'mode': 'rb'},
    {'ext': '.ppm', 'type': 'image/x-portable-pixmap', 'mode': 'rb'},
    {'ext': '.ppt', 'type': 'application/vnd.ms-powerpoint', 'mode': 'rb'},
    {'ext': '.ps', 'type': 'application/postscript', 'mode': 'rb'},
    {'ext': '.qt', 'type': 'video/quicktime', 'mode': 'rb'},
    {'ext': '.qti', 'type': 'image/x-quicktime', 'mode': 'rb'},
    {'ext': '.qtif', 'type': 'image/x-quicktime', 'mode': 'rb'},
    {'ext': '.ra', 'type': 'audio/x-pn-realaudio', 'mode': 'rb'},
    {'ext': '.ram', 'type': 'audio/x-pn-realaudio', 'mode': 'rb'},
    {'ext': '.ras', 'type': 'image/x-cmu-raster', 'mode': 'rb'},
    {'ext': '.rdf', 'type': 'application/rdf+xml', 'mode': 'rb'},
    {'ext': '.rgb', 'type': 'image/x-rgb', 'mode': 'rb'},
    {'ext': '.rm', 'type': 'application/vnd.rn-realmedia', 'mode': 'rb'},
    {'ext': '.roff', 'type': 'application/x-troff', 'mode': 'rb'},
    {'ext': '.rtf', 'type': 'text/rtf', 'mode': 'r'},
    {'ext': '.rtx', 'type': 'text/richtext', 'mode': 'r'},
    {'ext': '.sgm', 'type': 'text/sgml', 'mode': 'r'},
    {'ext': '.sgml', 'type': 'text/sgml', 'mode': 'r'},
    {'ext': '.sh', 'type': 'application/x-sh', 'mode': 'rb'},
    {'ext': '.shar', 'type': 'application/x-shar', 'mode': 'rb'},
    {'ext': '.silo', 'type': 'model/mesh', 'mode': 'rb'},
    {'ext': '.sit', 'type': 'application/x-stuffit', 'mode': 'rb'},
    {'ext': '.skd', 'type': 'application/x-koan', 'mode': 'rb'},
    {'ext': '.skm', 'type': 'application/x-koan', 'mode': 'rb'},
    {'ext': '.skp', 'type': 'application/x-koan', 'mode': 'rb'},
    {'ext': '.skt', 'type': 'application/x-koan', 'mode': 'rb'},
    {'ext': '.smi', 'type': 'application/smil', 'mode': 'rb'},
    {'ext': '.smil', 'type': 'application/smil', 'mode': 'rb'},
    {'ext': '.snd', 'type': 'audio/basic', 'mode': 'rb'},
    {'ext': '.so', 'type': 'application/octet-stream', 'mode': 'rb'},
    {'ext': '.spl', 'type': 'application/x-futuresplash', 'mode': 'rb'},
    {'ext': '.src', 'type': 'application/x-wais-source', 'mode': 'rb'},
    {'ext': '.sv4cpio', 'type': 'application/x-sv4cpio', 'mode': 'rb'},
    {'ext': '.sv4crc', 'type': 'application/x-sv4crc', 'mode': 'rb'},
    {'ext': '.svg', 'type': 'image/svg+xml', 'mode': 'rb'},
    {'ext': '.swf', 'type': 'application/x-shockwave-flash', 'mode': 'rb'},
    {'ext': '.t', 'type': 'application/x-troff', 'mode': 'rb'},
    {'ext': '.tar', 'type': 'application/x-tar', 'mode': 'rb'},
    {'ext': '.tcl', 'type': 'application/x-tcl', 'mode': 'rb'},
    {'ext': '.tex', 'type': 'application/x-tex', 'mode': 'rb'},
    {'ext': '.texi', 'type': 'application/x-texinfo', 'mode': 'rb'},
    {'ext': '.texinfo', 'type': 'application/x-texinfo', 'mode': 'rb'},
    {'ext': '.tif', 'type': 'image/tiff', 'mode': 'rb'},
    {'ext': '.tiff', 'type': 'image/tiff', 'mode': 'rb'},
    {'ext': '.tr', 'type': 'application/x-troff', 'mode': 'rb'},
    {'ext': '.tsv', 'type': 'text/tab-separated-values', 'mode': 'r'},
    {'ext': '.txt', 'type': 'text/plain', 'mode': 'r'},
    {'ext': '.ustar', 'type': 'application/x-ustar', 'mode': 'rb'},
    {'ext': '.vcd', 'type': 'application/x-cdlink', 'mode': 'rb'},
    {'ext': '.vrml', 'type': 'model/vrml', 'mode': 'rb'},
    {'ext': '.vxml', 'type': 'application/voicexml+xml', 'mode': 'rb'},
    {'ext': '.wav', 'type': 'audio/x-wav', 'mode': 'rb'},
    {'ext': '.wbmp', 'type': 'image/vnd.wap.wbmp', 'mode': 'rb'},
    {'ext': '.wbmxl', 'type': 'application/vnd.wap.wbxml', 'mode': 'rb'},
    {'ext': '.wml', 'type': 'text/vnd.wap.wml', 'mode': 'r'},
    {'ext': '.wmlc', 'type': 'application/vnd.wap.wmlc', 'mode': 'rb'},
    {'ext': '.wmls', 'type': 'text/vnd.wap.wmlscript', 'mode': 'r'},
    {'ext': '.wmlsc', 'type': 'application/vnd.wap.wmlscriptc', 'mode': 'rb'},
    {'ext': '.wrl', 'type': 'model/vrml', 'mode': 'rb'},
    {'ext': '.xbm', 'type': 'image/x-xbitmap', 'mode': 'rb'},
    {'ext': '.xht', 'type': 'application/xhtml+xml', 'mode': 'rb'},
    {'ext': '.xhtml', 'type': 'application/xhtml+xml', 'mode': 'rb'},
    {'ext': '.xls', 'type': 'application/vnd.ms-excel', 'mode': 'rb'},
    {'ext': '.xml', 'type': 'application/xml', 'mode': 'rb'},
    {'ext': '.xpm', 'type': 'image/x-xpixmap', 'mode': 'rb'},
    {'ext': '.xsl', 'type': 'application/xml', 'mode': 'rb'},
    {'ext': '.xslt', 'type': 'application/xslt+xml', 'mode': 'rb'},
    {'ext': '.xul', 'type': 'application/vnd.mozilla.xu+xml', 'mode': 'rb'},
    {'ext': '.xwd', 'type': 'image/x-xwindowdump', 'mode': 'rb'},
    {'ext': '.xyz', 'type': 'chemical/x-xyz', 'mode': 'rb'},
    {'ext': '.zip', 'type': 'application/zip', 'mode': 'rb'},
    {'ext': '.jpg', 'type': 'image/jpg', 'mode': 'rb'},
    {'ext': '.mp4', 'type': 'audio/mp4', 'mode': 'rb'},
    {'ext': '.js', 'type': " 'application/javascript", 'mode': 'r'},
    {'ext': '.ttf', 'type': 'application/x-font-ttf', 'mode': 'rb'},
    {'ext': '.woff2', 'type': 'application/x-font-woff2', 'mode': 'rb'},
    {'ext': '.woff', 'type': 'application/x-font-woff', 'mode': 'rb'},
    {'ext': '.wav', 'type': 'audio/wav', 'mode': 'rb'},
    {'ext': '.mpe', 'type': 'audio/mpeg', 'mode': 'rb'},
    {'ext': '.mpeg', 'type': 'audio/mpeg', 'mode': 'rb'},
    {'ext': '.json', 'type': 'application/json', 'mode': 'rb'}
]


HTTP_CODE = {
    "301" : "Moved Permanently",
    "307" : "Temporary Redirect",
    "400" : "Bad Request",
    "404" : "Not Found",
    "405" : "Method Not Allowed",
    
}