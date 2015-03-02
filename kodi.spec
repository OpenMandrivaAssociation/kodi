%define _libtag_ver %(version="`rpm -q --qf '%{VERSION}' libtag-devel`"; echo "$version")
%define _kodi_addons_dir %{_datadir}/kodi/addons
%define ffmpeg_archive_name 2.4.6-Helix
%define pvr_addons_archive_name Helix_rc3
%define build_cec 1
%define codename Helix

Summary:	XBMC Media Center - media player and home entertainment system
Name:		kodi
Version:	14.1
Release:	1
# nosefart audio plugin and RSXS-0.9 based screensavers are GPLv2 only
# several eventclients are GPLv3+ (in subpackages)
# libhdhomerun is LGPLv3+ with an exception (always ok to link against it)
# the rest is GPLv2+
# both GPLv2+ and GPLv2 are mentioned because plugins are not part of core
# xbmc and therefore e.g. /usr/bin/xbmc is GPLv2+ with LGPLv3+ part
# as allowed by a license exception
License:	GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
Group:		Video
Url:		http://kodi.tv/
Source0:	http://mirrors.xbmc.org/releases/source/%{version}-%{codename}.tar.gz
Source1:     	https://github.com/opdenkamp/xbmc-pvr-addons/archive/%{pvr_addons_archive_name}.tar.gz
Source2:     	https://github.com/xbmc/FFmpeg/archive/%{ffmpeg_archive_name}.tar.gz
Source3:	kodi.rpmlintrc

# PATCH-FIX-OPENSUSE -- enable all pvr addons
Patch0:      pvr-addons-enable-all.patch
Patch1:      no-xbmc-symbolic-link.patch
# https://bugs.mageia.org/show_bug.cgi?id=2331
# TODO: needs changes for upstreaming
Patch3:	0001-Fix-handling-of-filenames-with-spaces-in-wrapper-she.patch

#Other
#Patch4:		xbmc-13.0-external-ffmpeg.patch
#Patch5:		xbmc-13.0-no-win32.patch
# Display Music Videos in "Artist - Name" format instead of just "Name"
#Patch6:		xbmc-13.0-upnp-musicvideos-artist.patch
# Fix bug with UPnP playback for Playlists
#Patch7:		xbmc-13.0-upnp-playlists.patch

BuildRequires:	afpclient-devel
BuildRequires:	avahi-common-devel
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	crystalhd-devel
BuildRequires:	cwiid-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	lzo-devel
BuildRequires:	mysql-devel
BuildRequires:	python-devel
BuildRequires:	rtmp-devel
BuildRequires:	ssh-devel
BuildRequires:	tiff-devel
BuildRequires:	tinyxml-devel
BuildRequires:	yajl-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libcdio)
%if %{build_cec}
BuildRequires:	pkgconfig(libcec) >= 2:1:0
%else
BuildConflicts:	pkgconfig(libcec)
%endif
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmicrohttpd)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	pkgconfig(libnfs)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libshairport)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
# needed to delete the fixed rpath introduced by smbclient
BuildRequires:  chrpath

# pvr-addons
BuildRequires:  jsoncpp-devel
BuildRequires:  pkgconfig(cryptopp)
%ifarch %{ix86}
BuildRequires:	nasm
%endif
Requires:	lsb-release
# for codegenrator
BuildRequires:	doxygen
BuildRequires:	swig
BuildRequires:  byacc
BuildRequires:  yasm
BuildRequires:	gettext

# dlopened (existence check required by rpm5 as it doesn't use stderr):
%define dlopenreq() %([ -e %{_libdir}/lib%{1}.so ] && rpm -qf --qf '%%{name}' $(readlink -f %{_libdir}/lib%{1}.so) 2>/dev/null || echo %{name})
Requires:	%dlopenreq curl
Requires:	%dlopenreq FLAC
Requires:	%dlopenreq mad
Requires:	%dlopenreq ogg
Requires:	%dlopenreq vorbis
Requires:	%dlopenreq vorbisenc
Requires:	%dlopenreq vorbisfile
Requires:	%dlopenreq modplug
Requires:	%dlopenreq rtmp
Requires:	%dlopenreq mpeg2
Requires:	%dlopenreq ass
Requires:	%dlopenreq bluray
Requires:	%dlopenreq nfs
Requires:	%dlopenreq afpclient
Requires:	%dlopenreq plist
Requires:	%dlopenreq shairport
%if %{build_cec}
Requires:	%dlopenreq cec
%endif
# not nearly as common as the above, so just suggest instead for now:
Suggests:	%dlopenreq crystalhd
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
Suggests:	%{_lib}lame0
Suggests:	%{_lib}dvdcss2

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
%dir %{_libdir}/%{name}/system/players/paplayer
%{_libdir}/%{name}/%{name}.bin
%{_libdir}/%{name}/%{name}-xrandr
%dir %{_libdir}/%{name}/addons/*
%{_libdir}/%{name}/addons/*/*.so
%{_libdir}/%{name}/addons/*/*.vis
%{_libdir}/%{name}/addons/*/*.xbs
%{_libdir}/%{name}/addons/*/*.pvr
%{_libdir}/%{name}/system/ImageLib-*-linux.so
%{_libdir}/%{name}/system/hdhomerun-*-linux.so
%{_libdir}/%{name}/system/libcmyth-*-linux.so
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
%{_libdir}/%{name}/system/players/paplayer/libsidplay2-*-linux.so
%{_libdir}/%{name}/system/players/paplayer/nosefart-*-linux.so
%{_libdir}/%{name}/system/players/paplayer/stsoundlibrary-*-linux.so
%{_libdir}/%{name}/system/players/paplayer/timidity-*-linux.so
%{_libdir}/%{name}/system/players/paplayer/vgmstream-*-linux.so
%ifarch %ix86
%{_libdir}/%{name}/system/players/paplayer/SNESAPU-*-linux.so
%endif
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/addons
%{_datadir}/%{name}/FEH.py*
%{_datadir}/%{name}/language
%{_datadir}/%{name}/media
%{_datadir}/%{name}/sounds
%{_datadir}/%{name}/system
%{_datadir}/%{name}/userdata
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%package	devel
Summary:	Development files for XBMC
License:	GPLv2+
Group:		Development/C
Provides:	xbmc-eventclients-devel = %{EVRD}
Conflicts:	xbmc-eventclients-devel < 14.0
Obsoletes:	xbmc-eventclients-devel < 14.0
%rename		xbmc-devel

%description	devel
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build addons and eventclients.

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}/*.cmake

#----------------------------------------------------------------------------

%package	eventclients-common
Summary:	Common files for XBMC eventclients
License:	GPLv2+
Group:		Video
%rename		xbmc-eventclients-common

%description	eventclients-common
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains common files for eventclients.

%files eventclients-common
%python_sitelib/%{name}
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*.png

#----------------------------------------------------------------------------

%package	eventclient-wiiremote
Summary:	Wii Remote eventclient for XBMC
License:	GPLv3+
Group:		Video
Requires:	%{name}-eventclients-common = %{EVRD}
%rename		xbmc-eventclient-wiiremote

%description	eventclient-wiiremote
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%files eventclient-wiiremote
%{_bindir}/%{name}-wiiremote

#----------------------------------------------------------------------------

%package	eventclient-j2me
Summary:	J2ME eventclient for XBMC
License:	GPLv2+
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{EVRD}
%rename		xbmc-eventclient-j2me

%description	eventclient-j2me
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the J2ME eventclient, providing a bluetooth
server that can communicate with a mobile tool supporting J2ME.

%files eventclient-j2me
%{_bindir}/%{name}-j2meremote

#----------------------------------------------------------------------------

%package	eventclient-ps3
Summary:	PS3 eventclients for XBMC
License:	GPLv2+
Group:		Video
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{EVRD}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:	python-gobject avahi-python python-dbus
%rename		xbmc-eventclient-ps3

%description	eventclient-ps3
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%files eventclient-ps3
%{_bindir}/%{name}-ps3d
%{_bindir}/%{name}-ps3remote

#----------------------------------------------------------------------------

%package	eventclient-xbmc-send
Summary:	PS3 eventclient for XBMC
License:	GPLv2+
Group:		Video
Requires:	%{name}-eventclients-common = %{EVRD}
%rename		xbmc-eventclient-xbmc-send

%description	eventclient-xbmc-send
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the xbmc-send eventclient.

%files eventclient-xbmc-send
%{_bindir}/%{name}-send

#----------------------------------------------------------------------------

%prep
%setup -q -n xbmc-%{version}-%{codename} -a 1
%apply_patches

# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' -o -iname '*.jar' \) -print -delete

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

tar -xf %{SOURCE1}
mv xbmc-pvr-addons-%{pvr_addons_archive_name} pvr-addons
pushd pvr-addons
./bootstrap
popd

# Remove build time references so build-compare can do its work
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
FAKE_BUILDDATETIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes)

# remove it in ffmpeg archive and repackage it
tar xpfz %{SOURCE2} -C tools/depends/target/ffmpeg/
for file in tools/depends/target/ffmpeg/FFmpeg-%{ffmpeg_archive_name}/ffprobe.c tools/depends/target/ffmpeg/FFmpeg-%{ffmpeg_archive_name}/cmdutils.c; do
    sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" $file
done
tar cpfz tools/depends/target/ffmpeg/ffmpeg-%{ffmpeg_archive_name}.tar.gz -C tools/depends/target/ffmpeg/ FFmpeg-%{ffmpeg_archive_name}/
rm -r tools/depends/target/ffmpeg/FFmpeg-%{ffmpeg_archive_name}

# remove the remaining occurencies in the source tree
for file in lib/timidity/timidity/speex_a.c xbmc/Application.cpp xbmc/GUIInfoManager.cpp ; do
    sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" $file
done
for file in xbmc/interfaces/python/PythonSwig.cpp.template ; do
    sed -i -e "/PyModule_AddStringConstant.*__date__/ s/\${new Date()\.toString()}/$FAKE_BUILDDATETIME/"  $file
done

chmod +x bootstrap
./bootstrap
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ./bootstrap             
%build

# due to xbmc modules that use symbols from xbmc binary
# and are not using libtool
%define _disable_ld_no_undefined 1

# Workaround configure using git to override GIT_REV (TODO: fix it properly)
export ac_cv_prog_HAVE_GIT="no"

%configure \
	--enable-airplay \
	--enable-vdpau \
	--enable-vaapi \
	--enable-rtmp \
	--enable-libbluray \
	--disable-debug \
	--enable-shared \
	--enable-optimizations \
	--disable-static \
%if %{build_cec}
	--enable-libcec \
%endif
%ifarch %{arm}
	--enable-tegra --disable-neon \
%endif
	--enable-goom \
	--enable-pulse \
	--with-lirc-device=/var/run/lirc/lircd

# non-free = unrar
# dvdcss is handled via dlopen when disabled

%make
%make -C tools/EventClients wiimote

%install
%makeinstall_std
%makeinstall_std -C tools/EventClients

#remove the doc files from unversioned /usr/share/doc/kodi, they should be in versioned docdir
rm -r %{buildroot}/%{_datadir}/doc/

# copy manpages
install -m 644 -D docs/manpages/kodi-standalone.1 %{buildroot}%{_mandir}/man1/kodi-standalone.1
install -m 644 -D docs/manpages/kodi.bin.1 %{buildroot}%{_mandir}/man1/kodi.1

# remove win32 source files
rm -f %{buildroot}%{_kodi_addons_dir}/library.kodi.addon/dlfcn-win32.cpp
rm -f %{buildroot}%{_kodi_addons_dir}/library.kodi.addon/dlfcn-win32.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.xbmc.addon/dlfcn-win32.cpp
rm -f %{buildroot}%{_kodi_addons_dir}/library.xbmc.addon/dlfcn-win32.h

# remove duplicate header files
rm -f %{buildroot}%{_kodi_addons_dir}/library.kodi.addon/libXBMC_addon.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.xbmc.addon/libXBMC_addon.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.kodi.codec/libXBMC_codec.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.xbmc.codec/libXBMC_codec.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.kodi.gui/libXBMC_gui.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.xbmc.gui/libXBMC_gui.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.kodi.pvr/libXBMC_pvr.h
rm -f %{buildroot}%{_kodi_addons_dir}/library.xbmc.pvr/libXBMC_pvr.h

# delete fixed rpath from smbclient.pc - this fixes
# http://trac.kodi.tv/ticket/15497 and
# http://bugzilla.opensuse.org/show_bug.cgi?id=902421

chrpath %{buildroot}%{_libdir}/kodi/kodi.bin >/dev/null 2>&1 && \
chrpath -d %{buildroot}%{_libdir}/kodi/kodi.bin

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
		# so it results in no errors due to RTLD_LAZY being used by xbmc module loader.
		case $file:$symbol in */Euphoria.xbs:_ZN3PNG*) continue; esac
		# the symbol was not found
		undefined="${undefined}$file: $symbol\n"
	done
done
ok=1
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols!" && ok=
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && ok=
[ -n "$ok" ]
)
