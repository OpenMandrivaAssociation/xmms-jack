%define name xmms-jack
%define version 0.19
%define release %mkrel 8
%define jackversion 0.34.0

Summary: Xmms output plugin for the jack sound server
Name: %{name}
Version: %{version}
Epoch: 1
Release: %{release}
Source0: http://prdownloads.sourceforge.net/xmms-jack/%{name}-%{version}.tar.bz2
Patch0: xmms-jack-0.15-audacious.patch
Patch1: xmms-jack-fix-conflicting-function-name.patch
URL: https://sourceforge.net/projects/xmms-jack
# xmms-jack is GPL, bio2jack is LGPL
License: GPLv2+ and LGPLv2+
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libxmms-devel
BuildRequires: libjack-devel >= %jackversion
BuildRequires: libsamplerate-devel
BuildRequires: automake1.9
Requires: jackit  >= %jackversion
Requires: xmms

%description
XMMS audio output plugin for the jack audio
server(http://jackit.sourceforge.net).


%prep
%setup -q -n %name
%autopatch -p1
rm -f config.cache

%build
%configure2_5x
%make
mv .libs/libjackout.so libxmmsjackout.so


%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D libxmmsjackout.so %buildroot%_libdir/xmms/Output/libjackout.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS AUTHORS ChangeLog
%_libdir/xmms/Output/libjackout.so


