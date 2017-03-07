%define _disable_lto 1

%define branch_release	Krypton
%define version	17.0
%define snap	0
%define prel	0
%define rel	1

%if %snap
%define branch	%branch_release
%else
%define branch	%nil
%endif

%define branchr	%([ "%branch" ] && echo .%branch | tr - _)

%define tag	%{version}%([ "%prel" = "0" ] || echo "%prel" | sed s,beta,b,)-%{branch_release}

# build with internal ffmpeg, disabled by default (--with internal_ffmpeg)
%bcond_with	internal_ffmpeg

%if %with	internal_ffmpeg
# issue with 11.0 internal ffmpeg, haven't bothered with patching as it is
# not used in the default build anyway
%define Werror_cflags %nil
%endif

# Nightly-build mode (no patches, externally specified snapshot)
# (never enabled by default)
%if 0 && "%nightly_date" != "" && "%nightly_git" != "" && "%nightly_branch" != "" && "%nightly_rel" != ""
%define nightly	1
%define version	%nightly_date
%define rel	%nightly_rel
%else
%define nightly	0
%endif

Summary:	Kodi - media player and home entertainment system
Name:		kodi
Version:	%{version}
%if %nightly
Release:	%mkrel 1.%nightly_git.%nightly_branch.%rel
Source:		%{name}-%{nightly_date}-%{nightly_git}-%{nightly_branch}.tar.xz
%else
%if %snap
Release:	%mkrel 0.git%snap%branchr.%rel
Source:		%{name}-%branch_release-%snap.tar.xz
%else
%if %prel
Release:	%mkrel 0.%prel%branchr.%rel
#Source:		%%{name}-%%{version}-%%{branch_release}_%%{prel}.tar.gz
#Source:		%%{branch_release}_%%{prel}.tar.gz
# wget https://github.com/xbmc/xbmc/archive/14.0b3-Helix.tar.gz
Source:		https://github.com/xbmc/xbmc/archive/%tag.tar.gz
%else
%if "%branch" != ""
Release:	%mkrel 1.%branch.%rel
%else
Release:	%mkrel %rel
%endif
# Upstream tarballs seem to not be available yet... so:
# git archive --prefix=xbmc-13.0-Gotham/ 13.0-Gotham | xz > xbmc-13.0.tar.xz
#Source:		http://mirrors.xbmc.org/releases/source/%%{name}-%%{version}.tar.gz
Source:		http://mirrors.xbmc.org/releases/source/%{version}-%{branch_release}.tar.gz
%endif
%endif
%endif
Source2:	libdvdcss-master.tar.gz
Source3:	libdvdnav-master.tar.gz
Source4:	libdvdread-master.tar.gz

URL:		http://kodi.tv/

%if !%nightly

# Use system groovy
#Patch0:		xbmc-system-groovy.patch

# Disable --enable-static for TexturePacker configure when called as part of
# main configure as that would require we have static libraries of its dependencies
# installed
Patch1:		xbmc-texturepacker-no-static.patch
Patch2:		kodi-17.0-clang4.0.patch

# https://bugs.mageia.org/show_bug.cgi?id=2331
# TODO: needs changes for upstreaming
Patch214:	0001-Fix-handling-of-filenames-with-spaces-in-wrapper-she.patch

%endif

# nosefart audio plugin and RSXS-0.9 based screensavers are GPLv2 only
# several eventclients are GPLv3+ (in subpackages)
# libhdhomerun is LGPLv3+ with an exception (always ok to link against it)
# the rest is GPLv2+
# both GPLv2+ and GPLv2 are mentioned because plugins are not part of core
# xbmc and therefore e.g. /usr/bin/xbmc is GPLv2+ with LGPLv3+ part
# as allowed by a license exception
License:	GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
Group:		Video
BuildRequires:	boost-devel
%if %without internal_ffmpeg
BuildRequires:	ffmpeg-devel
%endif
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	libogg-devel
BuildRequires:	libwavpack-devel
BuildRequires:	python2-devel
BuildRequires:	glew-devel
BuildRequires:	pkgconfig(dvdnav)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	jpeg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libvorbis-devel
BuildRequires:	bzip2-devel
BuildRequires:	mysql-devel
BuildRequires:	lzo-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	fontconfig-devel
BuildRequires:	fribidi-devel
BuildRequires:	sqlite3-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig(libpcrecpp)
BuildRequires:	libcdio-devel
BuildRequires:	libmms-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	SDL_mixer-devel
BuildRequires:	jasper-devel
BuildRequires:	libtiff-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libalsa-devel
BuildRequires:	enca-devel
BuildRequires:	libxt-devel
BuildRequires:	libxtst-devel
BuildRequires:	libxmu-devel
BuildRequires:	libxinerama-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	dbus-devel
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pulseaudio-devel
BuildRequires:	avahi-common-devel
BuildRequires:	avahi-client-devel
BuildRequires:	libxrandr-devel
BuildRequires:	vdpau-devel
BuildRequires:	cwiid-devel
BuildRequires:	libice-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libmodplug-devel
BuildRequires:	ssh-devel
BuildRequires:	libva-devel
BuildRequires:	gettext-devel
BuildRequires:	expat-devel
BuildRequires:	libass-devel
BuildRequires:	rtmp-devel
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	bluez-devel
BuildRequires:	udev-devel
BuildRequires:	yajl-devel
BuildRequires:	nfs-devel
BuildRequires:	afpclient-devel
BuildRequires:	libplist-devel
#BuildRequires:	shairplay-devel
BuildRequires:	pkgconfig(libcec) >= 2.2
BuildRequires:	tinyxml-devel
BuildRequires:	pkgconfig(libxslt)
#BuildRequires:	pkgconfig(dcadec)
BuildRequires:	crossguid-devel
BuildRequires:	taglib-devel >= 1.8
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
# codegenerator.mk
# TODO: Something is wrong with java macros in mga2+, %java does not actually use java-rpmbuild
BuildRequires:	swig
BuildRequires:	groovy
BuildRequires:	apache-commons-lang
BuildRequires:	doxygen
BuildRequires:	yasm
# pvr-addons
BuildRequires:	jsoncpp-devel
BuildRequires:	pkgconfig(cryptopp)
%ifarch %ix86
BuildRequires:	nasm
%endif
# texturepacker
BuildRequires:	giflib-devel
Requires:	lsb-release
# dlopened (existence check required by rpm5 as it doesn't use stderr):
%define dlopenreq() %([ -e %{_libdir}/lib%{1}.so ] && rpm -qf --qf '%%{name}' $(readlink -f %{_libdir}/lib%{1}.so) 2>/dev/null || echo "xbmc-missing-buildrequires-on-%{1}")
Requires:	%dlopenreq curl
Requires:	%dlopenreq ogg
Requires:	%dlopenreq vorbis
Requires:	%dlopenreq vorbisfile
Requires:	%dlopenreq modplug
Requires:	%dlopenreq rtmp
Requires:	%dlopenreq mpeg2
Requires:	%dlopenreq ass
Requires:	%dlopenreq bluray
Requires:	%dlopenreq nfs
Requires:	%dlopenreq afpclient
Requires:	%dlopenreq plist
Requires:	%dlopenreq shairplay
Requires:	%dlopenreq cec
#Requires:	%dlopenreq dcadec
# TODO: FEH.py is useless nowadays, drop it here and upstream.
# for FEH.py, to check current configuration is ok for xbmc:
Requires:	xdpyinfo
Requires:	glxinfo
# for FEH.py to allow it to give an error message (should be available already
# on most systems):
Requires:	pygtk2.0
# for xbmc python scripts:
Requires:	python2-imaging
# Packages not shipped in core:
Suggests:	%{_lib}dvdcss2

# Packages have been merged
Obsoletes:	xbmc-core < 9.11-1.svn29468
Obsoletes:	xbmc-skin-confluence < 9.11-1.svn29468
Obsoletes:	xbmc-skin-pm3-hd < 9.11-1.svn29468
Obsoletes:	xbmc-nosefart < 9.11-1.svn29468
Obsoletes:	xbmc-screensavers-default < 9.11-1.svn29468
Obsoletes:	xbmc-script-examples < 9.11-1.svn27796
Obsoletes:	xbmc-web-pm3 < 9.11-1.svn27796

# Old name
%rename		xbmc

%description
Kodi (formerly known as XBMC) is an award-winning free and open source
software media player and entertainment hub for digital media.

While Kodi functions very well as a standard media player application
for your computer, it has been designed to be the perfect companion
for your HTPC. Supporting an almost endless range of remote controls,
and combined with its beautiful interface and powerful skinning
engine, Kodi feels very natural to use from the couch and is the
ideal solution for your home theater.

%if !%nightly
This is the stable version of Kodi from the %branch_release release branch.
Support for RAR files is not included due to license issues.
%endif

%package	eventclients-common
Summary:	Common files for Kodi eventclients
Group:		Video
License:	GPLv2+
BuildRequires:	python2
%rename		xbmc-eventclients-common

%description	eventclients-common
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains common files for eventclients.

%package	devel
Summary:	Development files for Kodi
Group:		Development/C
License:	GPLv2+
Provides:	xbmc-eventclients-devel = 12.3-10
Obsoletes:	xbmc-eventclients-devel < 12.3-10
%rename		xbmc-devel

%description	devel
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build addons and eventclients.

%package	eventclient-wiiremote
Summary:	Wii Remote eventclient for Kodi
Group:		Video
License:	GPLv3+
Requires:	%{name}-eventclients-common = %{version}-%{release}
%rename		xbmc-eventclient-wiiremote

%description	eventclient-wiiremote
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%package	eventclient-ps3
Summary:	PS3 eventclients for Kodi
Group:		Video
License:	GPLv2+
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:	python2-gobject python2-dbus
# TODO merge all these?, and TODO zeroconf.py to a correct package? :)
Obsoletes:	eventclient-ps3remote < 9.11-1.svn31936
%rename		xbmc-eventclient-ps3

%description	eventclient-ps3
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%package	eventclient-%{name}-send
Summary:	PS3 eventclient for Kodi
Group:		Video
License:	GPLv2+
Requires:	%{name}-eventclients-common = %{version}-%{release}
%rename		xbmc-eventclient-xbmc-send

%description	eventclient-%{name}-send
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the %{name}-send eventclient.

%prep
%if %nightly
%setup -q -n %name-%nightly_date-%nightly_git-%nightly_branch
%else
%if %snap
%setup -q -n %name-%branch_release-%snap
%else
%if %prel
%setup -q -n xbmc-%{tag}
%else
%setup -q -n xbmc-%{version}-%{branch_release}
%endif
%endif
%endif
%__cp %{SOURCE2}	tools/depends/target/libdvdcss/libdvdcss-master.tar.gz
%__cp %{SOURCE3}	tools/depends/target/libdvdnav/libdvdnav-master.tar.gz
%__cp %{SOURCE4}	tools/depends/target/libdvdread/libdvdread-master.tar.gz

%apply_patches
# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -print -delete

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

# py2 fix
sed -i 's/shell python/shell python2/' tools/EventClients/Makefile.in
%build
%if %nightly
export GIT_REV=%nightly_git
%else
%if %snap
export GIT_REV=%snap
%else
%if %prel
export GIT_REV=%tag
%else
export GIT_REV="tarball"
%endif
%endif
%endif

JAVA=%{java} CLASSPATH=$(build-classpath commons-lang) ./bootstrap

# due to xbmc modules that use symbols from xbmc binary
# and are not using libtool
%define _disable_ld_no_undefined 1

# Workaround configure using git to override GIT_REV (TODO: fix it properly)
export ac_cv_prog_HAVE_GIT="no"

%if %without internal_ffmpeg
# (Anssi 11/2014) Laazyyy.
# Kodi build assumes FFmpeg patched with ff_read_frame_flush() available as av_read_frame_flush().
# We have that patch but use a different name to signify that it is Kodi specific.
export CXXFLAGS="%optflags -Dav_read_frame_flush=av_read_frame_flush_mga_kodi_mod"
%endif

export PYTHON=%__python2
export PYTHON_VERSION=2

%configure2_5x \
%if %without internal_ffmpeg
	--with-ffmpeg=shared \
%endif
	--disable-debug \
	--disable-ccache \
	--disable-non-free \
	--disable-dvdcss \
	--enable-goom \
	--with-lirc-device=/var/run/lirc/lircd

# non-free = unrar
# dvdcss is handled via dlopen when disabled
# hal is disabled as it is just a fallback when the replacmenets are
# not available

%make
%make -C tools/EventClients wiimote

%install
%make_install
%make_install -C tools/EventClients

# unused
rm %{buildroot}%{_datadir}/xsessions/{xbmc,kodi}.desktop
# our version of the above:
install -d -m755 %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/15Kodi <<EOF
NAME=Kodi
ICON=%{name}.png
DESC=Kodi Media Center
EXEC=%{_bindir}/%{name}-standalone
SCRIPT:
exec %{_bindir}/%{name}-standalone
EOF

# unused files, TODO fix this upstream:
find %{buildroot}%{_datadir}/%{name}/addons/skin.*/media -name '*.png' -delete

# remove compat directory symlinks (RPM cannot handle dir=>symlink transition so
# more complex handling would be needed for these)
rm %{buildroot}%{_datadir}/xbmc
rm %{buildroot}%{_libdir}/xbmc
rm %{buildroot}%{_includedir}/xbmc

( # for IFS and +x
# Check for issues in ELF binaries
undefined=
fhserr=
echo Silencing output of undefined symbol and FHS conformance checks
set +x
IFS=$'\n'
for file in $(find %{buildroot} -type f); do
	type="$(file "$file")"
	echo "$type" | grep -q "ELF" || continue

	# Check that a binary file is not in datadir:
	echo "$file" | grep -q "%{_datadir}" && fhserr="${fhserr}$file\n"

	# check for undefined symbols in XBMC modules
	echo "$type" | grep -q "shared object" || continue
	for symbol in $(LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} ldd -r "$file" 2>&1 | grep undefined | awk '{ print $3 }'); do
		# undefined symbols may also be provided by XBMC:
		nm -f posix -D --no-demangle --defined-only %{buildroot}%{_libdir}/%{name}/%{name}.bin | grep -q "^$symbol " && continue
		# The symbol was not provided by XBMC.
		# Check if it is available through its dependencies:
		for filename in $(objdump -p %{buildroot}%{_libdir}/%{name}/%{name}.bin | grep NEEDED | awk '{ print $2 }'); do
			depfile="/%{_lib}/$filename"
			[ -e "$depfile" ] || depfile="%{_libdir}/$filename"
			nm -f posix -D --no-demangle --defined-only $depfile | grep -q "^$symbol " && continue 2
		done
		# Euphoria references rsxs PNG class, but it is never used at runtime,
		# so it results in no errors due to RTLD_LAZY being used by %{name} module loader.
		case $file:$symbol in
			*/Euphoria.xbs:_ZN3PNG*) continue;;
%if %with internal_ffmpeg
			*/dvdplayer/*.so:*) continue;;
%endif
		esac
		# the symbol was not found
		undefined="${undefined}$file: $symbol\n"
	done
done
ok=1
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols!" && ok=
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && ok=
[ -n "$ok" ]
)

%files
%doc %{_docdir}/%{name}
%{_sysconfdir}/X11/wmsession.d/15Kodi
%{_bindir}/%{name}
%{_bindir}/%{name}-standalone
# compat
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/addons
%dir %{_libdir}/%{name}/system
%dir %{_libdir}/%{name}/system/players
%dir %{_libdir}/%{name}/system/players/VideoPlayer
%{_libdir}/%{name}/%{name}.bin
%{_libdir}/%{name}/%{name}-xrandr
%dir %{_libdir}/%{name}/addons/*
%{_libdir}/%{name}/addons/*/*.so
%{_libdir}/%{name}/system/libcpluff-*-linux.so
%{_libdir}/%{name}/system/libexif-*-linux.so
%ifarch %ix86 x86_64
%{_libdir}/%{name}/system/libsse4-*-linux.so
%endif
%{_libdir}/%{name}/system/players/VideoPlayer/libdvd*-*-linux.so
%if %with internal_ffmpeg
%{_libdir}/%{name}/system/players/dvdplayer/av*-linux.so
%{_libdir}/%{name}/system/players/dvdplayer/postproc-*-linux.so
%{_libdir}/%{name}/system/players/dvdplayer/swscale-*-linux.so
%endif
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/privacy-policy.txt
%{_datadir}/%{name}/addons
%{_datadir}/%{name}/media
%{_datadir}/%{name}/system
%{_datadir}/%{name}/userdata
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%files eventclients-common
%python2_sitelib/%{name}
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*.png

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}/*.cmake

%files eventclient-ps3
%{_bindir}/%{name}-ps3d
%{_bindir}/%{name}-ps3remote

%files eventclient-%{name}-send
%{_bindir}/%{name}-send

%files eventclient-wiiremote
%{_bindir}/%{name}-wiiremote

