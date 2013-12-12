
Summary: Run command as root in a specified folder
Name:    %{name}
Version: 1.0.0
Release: %mkrel 1
Group:   File tools
License: GPLv2+
URL:     https://github.com/tarakbumba/caja-beesu
Source0: https://github.com/tarakbumba/caja-beesu/archive/%{name}-%{version}.tar.gz

BuildRequires:  intltool
BuildRequires:  mate-common >= 1.6.0
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libcaja-extension) >= 1.6.0

Requires:       beesu

%description
This is a proof-of-concept Caja extension which allows you to run
a command as root in arbitrary local folders.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
   --disable-static

%make

%install
%makeinstall_std

#we don't want these
rm -f %{buildroot}%{_libdir}/caja/extensions-2.0/*.la

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%{_libdir}/caja/extensions-2.0/libcaja-beesu.so

