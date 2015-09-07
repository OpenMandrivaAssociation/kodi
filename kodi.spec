%define _kodi_addons_dir %{_datadir}/kodi/addons
%define ffmpeg_archive_name 2.6.4-Isengard
%define pvr_addons_archive_name Helix_rc3
%define build_cec 0
%define codename Isengard
%define Werror_cflags %{nil}

Summary:	XBMC Media Center - media player and home entertainment system
Name:		kodi
Version:	15.1
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
Source1:	kodi.rpmlintrc
# Generated by:
#   cd xbmc-VERSION
#   sh ../download_pvr.sh
Source2:        pvr-addons.tar.bz2
Source3:        kodi-platform-054a42f66.tar.gz
Source4:	ffmpeg-%{ffmpeg_archive_name}.tar.gz
Patch1:         no-xbmc-symbolic-link.patch
# Raspberry Pi (armv6): omxplayer 3D support is only available for non X11 KODI
#Patch2:        disable_omxplayer_3d_support.patch
Patch3:         cmake_no_deps.patch
Patch4:         cmake_do_not_download.patch
Patch5:		cmake_build64.patch
Patch6:         kodi-texturepacker.patch
# PATCH-FIX-UPSTREAM: fix build with gcc5 (Tumbleweed)
Patch7:         kodi-15.0-gcc5.patch
#Patch8:		ffmpeg_autobuild_fix.patch

BuildRequires:	curl
BuildRequires:	afpclient-devel
BuildRequires:	avahi-common-devel
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
%ifarch %{ix86} x86_64
BuildRequires:	crystalhd-devel
%endif
BuildRequires:	cwiid-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	ffmpeg-static-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	lzo-devel
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig(python2)
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
BuildRequires:	pkgconfig(gpg-error)
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
BuildRequires:	pkgconfig(libcap)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	ungif-devel
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
# needed to delete the fixed rpath introduced by smbclient
BuildRequires:  chrpath
BuildRequires:	git

# pvr-addons
%if %mdvver >= 201500
BuildRequires:  jsoncpp-devel
%endif

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
BuildRequires:	java
#BuildRequires:  groovy

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
%dir %{_includedir}/kodi
%{_includedir}/kodi/DVDDemuxPacket.h
%{_includedir}/kodi/libXBMC_addon.h
%{_includedir}/kodi/libXBMC_codec.h
%{_includedir}/kodi/libXBMC_pvr.h
%{_includedir}/kodi/xbmc_addon_cpp_dll.h
%{_includedir}/kodi/xbmc_addon_dll.h
%{_includedir}/kodi/xbmc_addon_types.h
%{_includedir}/kodi/xbmc_codec_types.h
%{_includedir}/kodi/xbmc_epg_types.h
%{_includedir}/kodi/xbmc_pvr_dll.h
%{_includedir}/kodi/xbmc_pvr_types.h
%{_includedir}/kodi/xbmc_scr_dll.h
%{_includedir}/kodi/xbmc_scr_types.h
%{_includedir}/kodi/xbmc_stream_utils.hpp
%{_includedir}/kodi/xbmc_vis_dll.h
%{_includedir}/kodi/xbmc_vis_types.h
%{_includedir}/kodi/xbmc_audioenc_dll.h
%{_includedir}/kodi/xbmc_audioenc_types.h
%{_includedir}/kodi/AEChannelData.h
%{_includedir}/kodi/kodi_audiodec_dll.h
%{_includedir}/kodi/kodi_audiodec_types.h
%{_includedir}/kodi/libKODI_guilib.h


%package pvr.addons
Summary:        PVR Addons files for Kodi
Group:          Video
Requires:       %{name}
#Requires:       libjsoncpp1

%description pvr.addons
PVR Addons for Kodi Media Center

%files pvr.addons
%dir %{_libdir}/kodi
%dir %{_libdir}/kodi/addons/audiodecoder.modplug
%dir %{_libdir}/kodi/addons/audiodecoder.nosefart
%dir %{_libdir}/kodi/addons/audiodecoder.snesapu
%dir %{_libdir}/kodi/addons/audiodecoder.stsound
%dir %{_libdir}/kodi/addons/audiodecoder.timidity
%dir %{_libdir}/kodi/addons/audiodecoder.vgmstream
%dir %{_libdir}/kodi/addons/audioencoder.flac
%dir %{_libdir}/kodi/addons/audioencoder.lame
%dir %{_libdir}/kodi/addons/audioencoder.vorbis
%dir %{_libdir}/kodi/addons/audioencoder.wav
%dir %{_libdir}/kodi/addons/pvr.argustv
%dir %{_libdir}/kodi/addons/pvr.demo
%dir %{_libdir}/kodi/addons/pvr.dvblink
%dir %{_libdir}/kodi/addons/pvr.dvbviewer
%dir %{_libdir}/kodi/addons/pvr.filmon
%dir %{_libdir}/kodi/addons/pvr.hts
%dir %{_libdir}/kodi/addons/pvr.iptvsimple
%dir %{_libdir}/kodi/addons/pvr.mediaportal.tvserver
%dir %{_libdir}/kodi/addons/pvr.mythtv
%dir %{_libdir}/kodi/addons/pvr.nextpvr
%dir %{_libdir}/kodi/addons/pvr.njoy
%dir %{_libdir}/kodi/addons/pvr.pctv
%dir %{_libdir}/kodi/addons/pvr.stalker
%dir %{_libdir}/kodi/addons/pvr.vbox
%dir %{_libdir}/kodi/addons/pvr.vdr.vnsi
%dir %{_libdir}/kodi/addons/pvr.vuplus
%dir %{_libdir}/kodi/addons/pvr.wmc
%dir %{_datadir}/kodi
%dir %{_kodi_addons_dir}/audiodecoder.modplug
%dir %{_kodi_addons_dir}/audiodecoder.nosefart
%dir %{_kodi_addons_dir}/audiodecoder.snesapu
%dir %{_kodi_addons_dir}/audiodecoder.stsound
%dir %{_kodi_addons_dir}/audiodecoder.timidity
%dir %{_kodi_addons_dir}/audiodecoder.vgmstream
%dir %{_kodi_addons_dir}/audioencoder.flac
%dir %{_kodi_addons_dir}/audioencoder.lame
%dir %{_kodi_addons_dir}/audioencoder.vorbis
%dir %{_kodi_addons_dir}/audioencoder.wav
%dir %{_kodi_addons_dir}/pvr.argustv
%dir %{_kodi_addons_dir}/pvr.demo
%dir %{_kodi_addons_dir}/pvr.dvblink
%dir %{_kodi_addons_dir}/pvr.dvbviewer
%dir %{_kodi_addons_dir}/pvr.filmon
%dir %{_kodi_addons_dir}/pvr.hts
%dir %{_kodi_addons_dir}/pvr.iptvsimple
%dir %{_kodi_addons_dir}/pvr.mediaportal.tvserver
%dir %{_kodi_addons_dir}/pvr.mythtv
%dir %{_kodi_addons_dir}/pvr.nextpvr
%dir %{_kodi_addons_dir}/pvr.njoy
%dir %{_kodi_addons_dir}/pvr.pctv
%dir %{_kodi_addons_dir}/pvr.stalker
%dir %{_kodi_addons_dir}/pvr.vbox
%dir %{_kodi_addons_dir}/pvr.vdr.vnsi
%dir %{_kodi_addons_dir}/pvr.vuplus
%dir %{_kodi_addons_dir}/pvr.wmc
%{_libdir}/kodi/addons/audiodecoder.modplug/*
%{_libdir}/kodi/addons/audiodecoder.nosefart/*
%{_libdir}/kodi/addons/audiodecoder.snesapu/*
%{_libdir}/kodi/addons/audiodecoder.stsound/*
%{_libdir}/kodi/addons/audiodecoder.timidity/*
%{_libdir}/kodi/addons/audiodecoder.vgmstream/*
%{_libdir}/kodi/addons/audioencoder.flac/*
%{_libdir}/kodi/addons/audioencoder.lame/*
%{_libdir}/kodi/addons/audioencoder.vorbis/*
%{_libdir}/kodi/addons/audioencoder.wav/*
%{_libdir}/kodi/addons/pvr.argustv/*
%{_libdir}/kodi/addons/pvr.demo/*
%{_libdir}/kodi/addons/pvr.dvblink/*
%{_libdir}/kodi/addons/pvr.dvbviewer/*
%{_libdir}/kodi/addons/pvr.filmon/*
%{_libdir}/kodi/addons/pvr.hts/*
%{_libdir}/kodi/addons/pvr.iptvsimple/*
%{_libdir}/kodi/addons/pvr.mediaportal.tvserver/*
%{_libdir}/kodi/addons/pvr.mythtv/*
%{_libdir}/kodi/addons/pvr.nextpvr/*
%{_libdir}/kodi/addons/pvr.njoy/*
%{_libdir}/kodi/addons/pvr.pctv/*
%{_libdir}/kodi/addons/pvr.stalker/*
%{_libdir}/kodi/addons/pvr.vbox/*
%{_libdir}/kodi/addons/pvr.vdr.vnsi/*
%{_libdir}/kodi/addons/pvr.vuplus/*
%{_libdir}/kodi/addons/pvr.wmc/*
%{_kodi_addons_dir}/audiodecoder.modplug/*
%{_kodi_addons_dir}/audiodecoder.nosefart/*
%{_kodi_addons_dir}/audiodecoder.snesapu/*
%{_kodi_addons_dir}/audiodecoder.stsound/*
%{_kodi_addons_dir}/audiodecoder.timidity/*
%{_kodi_addons_dir}/audiodecoder.vgmstream/*
%{_kodi_addons_dir}/audioencoder.flac/*
%{_kodi_addons_dir}/audioencoder.lame/*
%{_kodi_addons_dir}/audioencoder.vorbis/*
%{_kodi_addons_dir}/audioencoder.wav/*
%{_kodi_addons_dir}/pvr.argustv/*
%{_kodi_addons_dir}/pvr.demo/*
%{_kodi_addons_dir}/pvr.dvblink/*
%{_kodi_addons_dir}/pvr.dvbviewer/*
%{_kodi_addons_dir}/pvr.filmon/*
%{_kodi_addons_dir}/pvr.hts/*
%{_kodi_addons_dir}/pvr.iptvsimple/*
%{_kodi_addons_dir}/pvr.mediaportal.tvserver/*
%{_kodi_addons_dir}/pvr.mythtv/*
%{_kodi_addons_dir}/pvr.nextpvr/*
%{_kodi_addons_dir}/pvr.njoy/*
%{_kodi_addons_dir}/pvr.pctv/*
%{_kodi_addons_dir}/pvr.stalker/*
%{_kodi_addons_dir}/pvr.vbox/*
%{_kodi_addons_dir}/pvr.vdr.vnsi/*
%{_kodi_addons_dir}/pvr.vuplus/*
%{_kodi_addons_dir}/pvr.wmc/*

Obsoletes:	eventclients-common
Obsoletes:	xbmc-eventclients-common
Obsoletes:	eventclient-wiiremote
Obsoletes:	xbmc-eventclient-wiiremote
Obsoletes:	eventclient-j2me
Obsoletes:	xbmc-eventclient-j2me
Obsoletes:	eventclient-ps3
Obsoletes:	xbmc-eventclient-ps3
Obsoletes:	eventclient-xbmc-send
Obsoletes:	xbmc-eventclient-xbmc-send

%prep
%setup -q -n xbmc-%{version}-%{codename}
%patch1
%ifarch x86_64
%patch4
%patch5
%endif

# Remove build time references so build-compare can do its work
#FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
#FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
#for file in xbmc/GUIInfoManager.cpp xbmc/Application.cpp; do
#  sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" $file
#done

# Fix the final version string showing as "exported"
# instead of the SVN revision number.
export HAVE_GIT="no" GIT_REV="exported"

# avoid long delays when powerkit isn't running
sed -i \
    -e '/dbus_connection_send_with_reply_and_block/s:-1:3000:' \
    xbmc/linux/*.cpp

### prep for pvr.addons
pushd project/cmake/addons
mkdir -p build/download
tar xvf %{SOURCE2} -C build/download
tar zxvf %{SOURCE3} --strip-components=1 -C depends/common/kodi-platform
# remove kodi-platform dependencies, because they are alreay installed
rm -f  depends/common/kodi-platform/deps.txt
rm -rf depends/common/tinyxml depends/common/platform
# We do not provide sidplay2 library on any SUSE distribution
rm -rf addons/audiodecoder.sidplay
popd
###

#add ffmpeg source

tar xpfz %{SOURCE4} -C tools/depends/target/ffmpeg/
tar cpfz tools/depends/target/ffmpeg/ffmpeg-%{ffmpeg_archive_name}.tar.gz -C tools/depends/target/ffmpeg/ FFmpeg-%{ffmpeg_archive_name}/
rm -r tools/depends/target/ffmpeg/FFmpeg-%{ffmpeg_archive_name}

%build
chmod +x bootstrap
./bootstrap

#ln -s %{_bindir}/python2 python
#export PATH=`pwd`:$PATH
export PYTHON_VERSION=2

export LDFLAGS="-Wl,--no-as-needed -ldl"

%configure \
    --with-ffmpeg=force \
    --enable-pulse 

%make

pushd project/cmake/addons
%cmake \
    -DBUILD_DIR=build \
    -DBUILD_SHARED_LIBS=1 \
    -DNEED_SUDO=FALSE \
    -DAPP_LIB_DIR=%{buildroot}%{_libdir}/kodi/ \
    -DCMAKE_INSTALL_LIBDIR=%{buildroot}%{_libdir}/kodi/ \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix}
%make

# Remove build time references so build-compare can do its work
#FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
#FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
#for file in audiodecoder.timidity/lib/timidity/timidity/speex_a.c; do
#    sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" $file
#done

popd

%install
%make_install 

# remove the doc files from unversioned /usr/share/doc/kodi, they should be in versioned docdir
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
rm -f %{buildroot}%{_kodi_addons_dir}/library.kodi.guilib/libKODI_guilib.h

%files
%doc copying.txt LICENSE.GPL docs/README.linux
%{_bindir}/kodi
%dir %{_libdir}/kodi
%{_libdir}/kodi/kodi.bin
%{_bindir}/kodi-standalone
%dir %{_libdir}/kodi/addons
%dir %{_libdir}/kodi/addons/library.xbmc.addon/
%{_libdir}/kodi/addons/library.xbmc.addon/*
%dir %{_libdir}/kodi/addons/library.xbmc.codec/
%{_libdir}/kodi/addons/library.xbmc.codec/*
%dir %{_libdir}/kodi/addons/library.xbmc.pvr/
%{_libdir}/kodi/addons/library.xbmc.pvr/*
%{_datadir}/xsessions/kodi.desktop
%{_datadir}/applications/kodi.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%dir %{_datadir}/kodi
%dir %{_datadir}/kodi/media
%dir %{_datadir}/kodi/system
%dir %{_libdir}/kodi/system
%dir %{_datadir}/kodi/userdata
%{_datadir}/kodi/media/*
%{_datadir}/kodi/system/*
%{_libdir}/kodi/system/*
%{_datadir}/kodi/userdata/*
%{_mandir}/man1/kodi.1.gz
%{_mandir}/man1/kodi-standalone.1.gz
%dir %{_kodi_addons_dir}
%dir %{_kodi_addons_dir}/metadata.album.universal/
%{_kodi_addons_dir}/metadata.album.universal/*
%dir %{_kodi_addons_dir}/metadata.artists.universal/
%{_kodi_addons_dir}/metadata.artists.universal/*
%dir %{_kodi_addons_dir}/metadata.common.allmusic.com/
%{_kodi_addons_dir}/metadata.common.allmusic.com/*
%dir %{_kodi_addons_dir}/metadata.common.fanart.tv/
%{_kodi_addons_dir}/metadata.common.fanart.tv/*
%dir %{_kodi_addons_dir}/metadata.common.htbackdrops.com/
%{_kodi_addons_dir}/metadata.common.htbackdrops.com/*
%dir %{_kodi_addons_dir}/metadata.common.imdb.com/
%{_kodi_addons_dir}/metadata.common.imdb.com/*
%dir %{_kodi_addons_dir}/metadata.common.last.fm/
%{_kodi_addons_dir}/metadata.common.last.fm/*
%dir %{_kodi_addons_dir}/metadata.common.musicbrainz.org/
%{_kodi_addons_dir}/metadata.common.musicbrainz.org/*
%dir %{_kodi_addons_dir}/metadata.common.theaudiodb.com/
%{_kodi_addons_dir}/metadata.common.theaudiodb.com/*
%dir %{_kodi_addons_dir}/metadata.common.themoviedb.org/
%{_kodi_addons_dir}/metadata.common.themoviedb.org/*
%dir %{_kodi_addons_dir}/metadata.local/
%{_kodi_addons_dir}/metadata.local/*
%dir %{_kodi_addons_dir}/metadata.musicvideos.theaudiodb.com/
%{_kodi_addons_dir}/metadata.musicvideos.theaudiodb.com/*
%dir %{_kodi_addons_dir}/metadata.themoviedb.org/
%{_kodi_addons_dir}/metadata.themoviedb.org/*
%dir %{_kodi_addons_dir}/metadata.tvdb.com/
%{_kodi_addons_dir}/metadata.tvdb.com/*
%dir %{_kodi_addons_dir}/repository.xbmc.org/
%{_kodi_addons_dir}/repository.xbmc.org/*
%dir %{_kodi_addons_dir}/resource.uisounds.confluence/
%{_kodi_addons_dir}/resource.uisounds.confluence/*
%dir %{_libdir}/kodi/addons/screensaver.rsxs.euphoria/
%{_libdir}/kodi/addons/screensaver.rsxs.euphoria/*
%dir %{_kodi_addons_dir}/screensaver.rsxs.euphoria/
%{_kodi_addons_dir}/screensaver.rsxs.euphoria/*
%dir %{_libdir}/kodi/addons/screensaver.rsxs.plasma/
%{_libdir}/kodi/addons/screensaver.rsxs.plasma/*
%dir %{_kodi_addons_dir}/screensaver.rsxs.plasma/
%{_kodi_addons_dir}/screensaver.rsxs.plasma/*
%dir %{_libdir}/kodi/addons/screensaver.rsxs.solarwinds/
%{_libdir}/kodi/addons/screensaver.rsxs.solarwinds/*
%dir %{_kodi_addons_dir}/screensaver.rsxs.solarwinds/
%{_kodi_addons_dir}/screensaver.rsxs.solarwinds/*
%dir %{_kodi_addons_dir}/screensaver.xbmc.builtin.black/
%{_kodi_addons_dir}/screensaver.xbmc.builtin.black/*
%dir %{_kodi_addons_dir}/screensaver.xbmc.builtin.dim/
%{_kodi_addons_dir}/screensaver.xbmc.builtin.dim/*
%dir %{_kodi_addons_dir}/script.module.pil/
%{_kodi_addons_dir}/script.module.pil/*
%dir %{_kodi_addons_dir}/service.xbmc.versioncheck/
%{_kodi_addons_dir}/service.xbmc.versioncheck/*
%dir %{_kodi_addons_dir}/skin.confluence/
%{_kodi_addons_dir}/skin.confluence/*
%dir %{_libdir}/kodi/addons/visualization.fishbmc/
%{_libdir}/kodi/addons/visualization.fishbmc/*
%dir %{_kodi_addons_dir}/visualization.fishbmc/
%{_kodi_addons_dir}/visualization.fishbmc/*
%dir %{_libdir}/kodi/addons/visualization.glspectrum/
%{_libdir}/kodi/addons/visualization.glspectrum/*
%dir %{_kodi_addons_dir}/visualization.glspectrum/
%{_kodi_addons_dir}/visualization.glspectrum/*
%dir %{_libdir}/kodi/addons/visualization.goom/
%{_libdir}/kodi/addons/visualization.goom/*
%dir %{_kodi_addons_dir}/visualization.goom/
%{_kodi_addons_dir}/visualization.goom/*
%dir %{_libdir}/kodi/addons/visualization.projectm/
%{_libdir}/kodi/addons/visualization.projectm/*
%dir %{_kodi_addons_dir}/visualization.projectm/
%{_kodi_addons_dir}/visualization.projectm/*
%dir %{_kodi_addons_dir}/visualization.vortex/
%{_kodi_addons_dir}/visualization.vortex/*
%dir %{_libdir}/kodi/addons/visualization.waveform/
%{_libdir}/kodi/addons/visualization.waveform/*
%dir %{_kodi_addons_dir}/visualization.waveform/
%{_kodi_addons_dir}/visualization.waveform/*
%dir %{_kodi_addons_dir}/webinterface.default/
%{_kodi_addons_dir}/webinterface.default/*
%dir %{_kodi_addons_dir}/xbmc.codec/
%{_kodi_addons_dir}/xbmc.codec/*
%dir %{_kodi_addons_dir}/xbmc.addon/
%{_kodi_addons_dir}/xbmc.addon/*
%dir %{_kodi_addons_dir}/xbmc.core/
%{_kodi_addons_dir}/xbmc.core/*
%dir %{_kodi_addons_dir}/xbmc.gui/
%{_kodi_addons_dir}/xbmc.gui/*
%dir %{_kodi_addons_dir}/xbmc.json/
%{_kodi_addons_dir}/xbmc.json/*
%dir %{_kodi_addons_dir}/xbmc.metadata/
%{_kodi_addons_dir}/xbmc.metadata/*
%dir %{_kodi_addons_dir}/xbmc.pvr/
%{_kodi_addons_dir}/xbmc.pvr/*
%dir %{_kodi_addons_dir}/xbmc.python/
%{_kodi_addons_dir}/xbmc.python/*
%dir %{_kodi_addons_dir}/audioencoder.xbmc.builtin.aac/
%{_kodi_addons_dir}/audioencoder.xbmc.builtin.aac/*
%dir %{_kodi_addons_dir}/audioencoder.xbmc.builtin.wma/
%{_kodi_addons_dir}/audioencoder.xbmc.builtin.wma/*
%dir %{_kodi_addons_dir}/kodi.audiodecoder/
%{_kodi_addons_dir}/kodi.audiodecoder/*
%dir %{_kodi_addons_dir}/kodi.guilib/
%{_kodi_addons_dir}/kodi.guilib/*
%dir %{_kodi_addons_dir}/kodi.resource/
%{_kodi_addons_dir}/kodi.resource/*
%dir %{_kodi_addons_dir}/resource.language.en_gb/
%{_kodi_addons_dir}/resource.language.en_gb/*
%dir %{_kodi_addons_dir}/xbmc.audioencoder/
%{_kodi_addons_dir}/xbmc.audioencoder/*
%dir %{_kodi_addons_dir}/xbmc.webinterface/
%{_kodi_addons_dir}/xbmc.webinterface/*
%{_libdir}/kodi/addon-helpers.cmake
%{_libdir}/kodi/addoptions.cmake
%{_libdir}/kodi/check_target_platform.cmake
%{_libdir}/kodi/handle-depends.cmake
%{_libdir}/kodi/kodi-config.cmake
%{_libdir}/kodi/prepare-env.cmake
%{_libdir}/kodi/xbmc-config.cmake
%dir %{_libdir}/kodi/addons/library.kodi.guilib/
%{_libdir}/kodi/addons/library.kodi.guilib/*
