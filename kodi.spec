%define branch_release	Jarvis
%define version	16.1
%define snap	0
%define prel	0
%define rel	3

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
# (cg) From https://github.com/opdenkamp/xbmc-pvr-addons
# git archive --prefix=pvr-addons/ origin/master | xz
Source1:	xbmc-pvr-addons-28f0e74864791cb9bb123559acb3d82e995b2b80.tar.xz
URL:		http://kodi.tv/

%if !%nightly

# Use system groovy
Patch0:		xbmc-system-groovy.patch

# Disable --enable-static for TexturePacker configure when called as part of
# main configure as that would require we have static libraries of its dependencies
# installed
Patch1:		xbmc-texturepacker-no-static.patch

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
Group:		Video/Players
BuildRequires:	boost-devel
%if %without internal_ffmpeg
BuildRequires:	ffmpeg-devel
%endif
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	libogg-devel
BuildRequires:	libwavpack-devel
BuildRequires:	python-devel
BuildRequires:	glew-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	libjpeg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libvorbis-devel
BuildRequires:	bzip2-devel
BuildRequires:	mysql-devel
BuildRequires:	liblzo-devel
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
BuildRequires:	libjasper-devel
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
BuildRequires:	libx11-devel
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
BuildRequires:	shairplay-devel
BuildRequires:	pkgconfig(libcec) >= 2.2
BuildRequires:	tinyxml-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(dcadec)
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
Requires:	%dlopenreq dcadec
# TODO: FEH.py is useless nowadays, drop it here and upstream.
# for FEH.py, to check current configuration is ok for xbmc:
Requires:	xdpyinfo
Requires:	glxinfo
# for FEH.py to allow it to give an error message (should be available already
# on most systems):
Requires:	pygtk2
# for xbmc python scripts:
Requires:	python-imaging
# Packages not shipped in core:
Recommends:	%{_lib}dvdcss2

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
Group:		Video/Players
License:	GPLv2+
BuildRequires:	python
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
Group:		Video/Players
License:	GPLv3+
Requires:	%{name}-eventclients-common = %{version}-%{release}
%rename		xbmc-eventclient-wiiremote

%description	eventclient-wiiremote
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%package	eventclient-j2me
Summary:	J2ME eventclient for Kodi
Group:		Video/Players
License:	GPLv2+
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}
%rename		xbmc-eventclient-j2me

%description	eventclient-j2me
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the J2ME eventclient, providing a bluetooth
server that can communicate with a mobile tool supporting J2ME.

%package	eventclient-ps3
Summary:	PS3 eventclients for Kodi
Group:		Video/Players
License:	GPLv2+
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:	python-gobject avahi-python python-dbus
# TODO merge all these?, and TODO zeroconf.py to a correct package? :)
Obsoletes:	eventclient-ps3remote < 9.11-1.svn31936
%rename		xbmc-eventclient-ps3

%description	eventclient-ps3
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%package	eventclient-%{name}-send
Summary:	PS3 eventclient for Kodi
Group:		Video/Players
License:	GPLv2+
Requires:	%{name}-eventclients-common = %{version}-%{release}
%rename		xbmc-eventclient-xbmc-send

%description	eventclient-%{name}-send
Kodi is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the %{name}-send eventclient.

%prep
%if %nightly
%setup -q -n %name-%nightly_date-%nightly_git-%nightly_branch -a 1
%else
%if %snap
%setup -q -n %name-%branch_release-%snap -a 1
%else
%if %prel
%setup -q -n xbmc-%{tag} -a 1
%else
%setup -q -n xbmc-%{version}-%{branch_release} -a 1
%endif
%endif
%endif
%autopatch -p1
# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' -o -iname '*.jar' \) -print -delete

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

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

pushd pvr-addons
./bootstrap
popd

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

# (cg) We cannot enable MythTV support easily via a passthrough configure from above
#      so re-run configure here and explicitly pass the --enable-addons-with-dependencies option
pushd pvr-addons
%configure2_5x \
	--enable-addons-with-dependencies
popd

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
%dir %{_libdir}/%{name}/system/players/dvdplayer
%{_libdir}/%{name}/%{name}.bin
%{_libdir}/%{name}/%{name}-xrandr
%dir %{_libdir}/%{name}/addons/*
%{_libdir}/%{name}/addons/*/*.so
%{_libdir}/%{name}/system/ImageLib-*-linux.so
%{_libdir}/%{name}/system/libcpluff-*-linux.so
%{_libdir}/%{name}/system/libexif-*-linux.so
%ifarch %ix86 x86_64
%{_libdir}/%{name}/system/libsse4-*-linux.so
%endif
%{_libdir}/%{name}/system/players/dvdplayer/libdvdnav-*-linux.so
%if %with internal_ffmpeg
%{_libdir}/%{name}/system/players/dvdplayer/av*-linux.so
%{_libdir}/%{name}/system/players/dvdplayer/postproc-*-linux.so
%{_libdir}/%{name}/system/players/dvdplayer/swscale-*-linux.so
%endif
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/addons
%{_datadir}/%{name}/media
%{_datadir}/%{name}/system
%{_datadir}/%{name}/userdata
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%files eventclients-common
%python_sitelib/%{name}
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*.png

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}/*.cmake

%files eventclient-j2me
%{_bindir}/%{name}-j2meremote

%files eventclient-ps3
%{_bindir}/%{name}-ps3d
%{_bindir}/%{name}-ps3remote

%files eventclient-%{name}-send
%{_bindir}/%{name}-send

%files eventclient-wiiremote
%{_bindir}/%{name}-wiiremote


%changelog
* Sat Jun 25 2016 anssi <anssi> 16.1-3.mga6
+ Revision: 1037684
- Add BuildRequires on mesaglesv2-devel, used by default on some platforms

* Sat Jun 25 2016 anssi <anssi> 16.1-2.mga6
+ Revision: 1037658
- Fix missing skin textures due to missing TexturePacker
  (add xbmc-texturepacker-no-static.patch and BR on giflib-devel)

* Wed May 04 2016 daviddavid <daviddavid> 16.1-1.mga6
+ Revision: 1009156
- new version: 16.1 (Jarvis)

* Thu Apr 28 2016 daviddavid <daviddavid> 16.0-2.mga6
+ Revision: 1007228
- rebuild with new libnfs 1.9.8

* Mon Mar 21 2016 daviddavid <daviddavid> 16.0-1.mga6
+ Revision: 993463
- new version: 16.0 (Jarvis)
- rediff patch 0 and patch 214
- remove patch 1 and patch 200
- add BRs pkgconfig(dcadec) and crossguid-devel
- update files list
- rebuild for new glew 1.13

  + umeabot <umeabot>
    - Mageia 6 Mass Rebuild

* Thu Jul 16 2015 sander85 <sander85> 14.2-2.mga6
+ Revision: 854808
- Rebuild for new libcdio

* Sat Jun 27 2015 buchan <buchan> 14.2-1.mga6
+ Revision: 846355
- New version 14.2

* Wed Jun 24 2015 akien <akien> 14.0-3.mga6
+ Revision: 842012
- Rebuild for GLEW 1.12

* Wed May 13 2015 neoclust <neoclust> 14.0-2.mga5
+ Revision: 822031
- Add patch to fix CVE-2015-3885

* Tue Dec 30 2014 anssi <anssi> 14.0-1.mga5
+ Revision: 807229
- new version 14.0 final
- update pvr addons
- drop Wformat-security patch, applied upstream

* Thu Nov 27 2014 anssi <anssi> 14.0-0.beta5.1.mga5
+ Revision: 799636
- new version 14.0 beta5

* Tue Nov 25 2014 anssi <anssi> 14.0-0.beta4.2.mga5
+ Revision: 799183
- remove rename compatibility symlinks for directories to allow for
  xbmx => kodi upgrade, since they are not needed (the executable
  compatibility symlinks are kept)

* Mon Nov 24 2014 anssi <anssi> 14.0-0.beta4.1.mga5
+ Revision: 798851
- new version 14.0 beta4

* Mon Nov 24 2014 anssi <anssi> 14.0-0.beta3.1.mga5
+ Revision: 798730
- new version 14.0 beta3
- rename to kodi as per upstream (upstream compatibility symlinks remain)
- depend on shairplay instead of shairport
- use SDL 2.0 instead of 1.x
- bump dependency on libcec
- buildrequires jsoncpp-devel and cryptopp-devel for pvr-addons
- drop obsolete dependencies
- fix -Werror=format-security issue in pvr-addons (submitted upstream)
- drop bootstrap-return-value.patch, applied upstream

  + tv <tv>
    - drop useless BR on java-rpmbuild
    - rebuild for missing pythoneggs deps
    - s/uggests:/Recommends:/

  + umeabot <umeabot>
    - Second Mageia 5 Mass Rebuild
    - Mageia 5 Mass Rebuild

  + buchan <buchan>
    - Version 13.2
    - Update pvr addon to current git

  + pterjan <pterjan>
    - Rebuild for new Python

* Mon May 05 2014 colin <colin> 13.0-1.mga5
+ Revision: 620228
- Add missing BR for yasm
- Add missing BR for libxslt
- Fix up the objectweb-asm3 class path for mga5+
- New version: 13 - Gotham
- Drop upstream patches
- Rediff still applicable downstream patches
- Add format-security patch for pvr-addons (should be upstreamed)
- Temporarily disable db-upgrade patch (may no longer be needed)
- Switch to generic -devel package (rather than eventclients-devel)

  + fwang <fwang>
    - rebuild for new libplist
    - rebuild for new ffmpeg

  + daviddavid <daviddavid>
    - rebuild for new libplist

* Mon Feb 17 2014 colin <colin> 12.3-6.mga5
+ Revision: 593528
- Update to latest PVR addons (adds support for MythTV 0.27)

* Sun Feb 16 2014 luigiwalser <luigiwalser> 12.3-5.mga5
+ Revision: 592550
- rebuild for librtmp

* Sat Feb 15 2014 luigiwalser <luigiwalser> 12.3-4.mga5
+ Revision: 592294
- rebuild for libcdio and libass

* Sun Feb 09 2014 anssi <anssi> 12.3-3.mga5
+ Revision: 587527
- fix CVE-2013-1438 (denial of service via a crafted photo file)

* Wed Feb 05 2014 anssi <anssi> 12.3-2.mga5
+ Revision: 583415
- fix AC-3 encoding for S/PDIF with recent FFmpeg (patches from upstream)

  + colin <colin>
    - Update to 12.3 bugfix release + latest PVR addons

* Sun Nov 24 2013 colin <colin> 12.2-6.mga4
+ Revision: 552712
- Update to latest pvr-addons

* Tue Oct 22 2013 umeabot <umeabot> 12.2-5.mga4
+ Revision: 546083
- Mageia 4 Mass Rebuild

* Thu Oct 17 2013 luigiwalser <luigiwalser> 12.2-4.mga4
+ Revision: 502119
- include FEH.py[co] in files list

* Wed Sep 11 2013 anssi <anssi> 12.2-3.mga4
+ Revision: 477758
- fix various A/V sync issues (patch from upstream,
  0001-SoftAE-Fix-A-V-sync-issues-caused-by-wrong-buffer-ti.patch)
- fix crash on encoder initialization failure (patch from upstream,
  0001-Fix-crash-when-audio-encoder-is-not-initalized.patch)
- fix build with current ffmpeg (various patches from upstream,
  fixes mga #10973)
- fix zombie process issues causing video playback issues with
  NVIDIA proprietary driver 317+ (from upstream, fixes mga #10485)
- fix handling of file names with spaces in the wrapper script
  (fixes mga #2331)

  + fwang <fwang>
    - rebuild for new ffmpeg

* Tue Jul 09 2013 fwang <fwang> 12.2-2.mga4
+ Revision: 451608
- rebuild for new boost

* Sun Jun 02 2013 colin <colin> 12.2-1.mga4
+ Revision: 435328
- New version: 12.2
- Update to lates pvr addons

* Sat Mar 30 2013 colin <colin> 12.1-2.mga3
+ Revision: 406674
- Update PVR addons to latest frodo branch.
- Disable PA support for now as not yet fully stable (still works fine via ALSA->PA layer)

* Fri Mar 29 2013 colin <colin> 12.1-1.mga3
+ Revision: 406450
- Switch pvr-addons tarball to the 12.0-Frodo tag from git.
- Package PVR Addons
- Revert patch from PVR Addons that is unsynced from main xbmc
- Enable PulseAudio support
- New version: 12.1

* Sat Mar 02 2013 anssi <anssi> 12.0-1.mga3
+ Revision: 400965
- 12.0 "frodo" final version
- drop automake1.13.patch, fixed upstream
- fix buildrequires for better backportability

* Mon Jan 14 2013 umeabot <umeabot> 12.0-0.rc3.2.mga3
+ Revision: 386607
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Wed Jan 09 2013 anssi <anssi> 12.0-0.rc3.1.mga3
+ Revision: 343733
- new version 12.0 rc3 (Frodo)
- drop merged FFmpeg support backport patches
- rediff old upgrade workaround patch
- use system groovy (system-groovy.patch)
- workaround a code generator issue when using system groovy
  (system-groovy-hack.patch)
- fix bootstrap return value in case of autotools error
  (bootstrap-return-value.patch)
- fix build with automake 1.13+ (automake1.13.patch)
- add new buildrequires
- drop PVR patch, merged upstream
  o NOTE: PVR addons are no longer bundled but instead have to be
    installed separately

  + fwang <fwang>
    - br pcrecpp
    - update rpm group
    - rebuild for new ffmpeg

* Thu Aug 30 2012 fwang <fwang> 11.0-1.pvr.5.mga3
+ Revision: 285685
- rebuild for new glew

* Thu Aug 02 2012 fwang <fwang> 11.0-1.pvr.4.mga3
+ Revision: 277861
- rebuild for new glew

* Tue Jul 10 2012 anssi <anssi> 11.0-1.pvr.3.mga3
+ Revision: 269300
- fix missing include in wiiremote eventclient
  (wiiremote-missing-include.patch)
- backport FFmpeg support patches to allow build with cauldron ffmpeg
  (patches 101..145)

  + colin <colin>
    - Rebuild against new libudev major

* Fri Mar 30 2012 anssi <anssi> 11.0-1.pvr.2.mga2
+ Revision: 227542
- update PVR patchset to opdenkamp's final 11.0-Eden-pvr tag
- drop obsoleted HAL support (XBMC supports the newer replacements fine;
  reported by Damien Lallement)
- add support for building the package with the bundled ffmpeg using
  --with internal_ffmpeg (not enabled by default)

* Sat Mar 24 2012 anssi <anssi> 11.0-1.pvr.1.mga2
+ Revision: 226110
- XBMC 11.0 Eden final
- update PVR patchset snapshot
- drop patches applied upstream (libpng1.5 build fix, archived subtitle
  loading fix)

* Sat Mar 17 2012 anssi <anssi> 11.0-0.rc2.pvr.3.mga2
+ Revision: 223735
- do not load non-matching subtitles from archives (upstream ticket
  12719, fixed-don-t-load-non-matching-archived-subtitles-fix.patch,
  applied upstream)
- add a workaround for upgrading from old incompatible addon database
  (hack-workaround-for-old-incompatible-PVR-addon-datab.patch)

* Mon Mar 05 2012 anssi <anssi> 11.0-0.rc2.pvr.2.mga2
+ Revision: 219397
- enable Pulse-Eight CEC adapter support via libcec
- use "tarball" for git revision, tarball name is too long
- update .spec comments

* Sat Mar 03 2012 anssi <anssi> 11.0-0.rc2.pvr.1.mga2
+ Revision: 217508
- new version 11.0 rc2 (PVR-patched)
- build against system python
- update license tags and description
- build against udev, yajl, libnfs, libafpclient, libplist, libshairport
- add run-time dependencies on libass and libmpeg2
- upgrade libbluray to a hard dependency
- drop requirement on python-sqlite2, it is no longer used
- drop suggestion on libdca, it is no longer used
- faac and xbms are no longer used, drop mentions of them
- fix build with libpng1.5 (libpng-1.5.patch by Zenkibou) and switch to it
  (dropping use-libpng12.patch)
- fix undefined symbols in MythTV PVR client
  (fixed-undefined-symbols-in-MythTV-PVR-client.patch)
- drop bundled python build support, upstream has dropped support for it
- drop backport patches, patches applied upstream, and patches for the
  previously bundled python
- drop a workaround for the NVIDIA proprietary driver version 260.x.y
  (workaround-for-crash-with-nonpulse-nvidia260.patch)
- use the mainline addon database instead of Addons2.db as the PVR patch
  no longer causes incompatibility (dropped
  changed-use-the-legacy-pvr-testing2-addon-database.patch)
- drop workaround for 23.976 fps mkv files which was needed only on
  Mandriva 2010.1 and older (dropped old-libavformat-mkv-subs.patch)
- drop faad support workaround, faad is no longer used (dropped
  hack-ext-faad-with-int-headers.patch)

* Mon Dec 05 2011 anssi <anssi> 10.1-1.pvr.4.mga2
+ Revision: 176796
- link wiiremote eventclient with -lbluetooth (link-bluetooth.patch,
  fixes build)
- fix some cases of libpng15 being used instead of libpng12, causing
  XBMC to fail to start due to conflicts between libpng12 and libpng15
  as some parts were built against libpng12 (as they do not build with
  libpng15)

* Thu Nov 03 2011 anssi <anssi> 10.1-1.pvr.3.mga2
+ Revision: 162472
- fix build with current FFmpeg
  o 12 patches backported from upstream git master
  o xbmc-pvr-new-ffmpeg.patch
- build with libpng12 instead of libpng (fixes build)
- renumber patches
- fix grammar of a .spec comment

* Sat Apr 30 2011 anssi <anssi> 10.1-1.pvr.2.mga1
+ Revision: 93516
- fix reported version

* Wed Apr 20 2011 anssi <anssi> 10.1-1.pvr.1.mga1
+ Revision: 89302
- new bugfix release 10.1
- drop allow-ppp.patch, fixed upstream
- rediff pvr patch

* Sun Mar 27 2011 ennael <ennael> 10.0-1.pvr.4.mga1
+ Revision: 78144
- clean spec file
- imported package xbmc

