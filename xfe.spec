Summary:	X File Explorer (Xfe) is a filemanager for X
Summary(pl.UTF-8):	X File Explorer - zarządca plików dla X
Name:		xfe
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/File
Source0:	https://downloads.sourceforge.net/project/xfe/xfe/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	5ec269a168dab95310841710811e0915
URL:		http://roland65.free.fr/xfe/
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	fox16-devel >= 1.6
BuildRequires:	freetype-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxcb-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	polkit-devel
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel
Requires:	fox16 >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X File Explorer (Xfe) is a filemanager for X. It is based on the
popular X Win Commander, which is discontinued. Xfe is desktop
independent and is written with the C++ Fox Toolkit. It has Windows
Commander or MS-Explorer look and is very fast and simple.

%description -l pl.UTF-8
X File Explorer (Xfe) to zarządca plików dla systemu X Window. Jest
oparty na popularnym X Win Commander, który nie jest już rozwijany.
Xfe jest niezależny od desktopu, jest napisany za pomocą C++ Fox
Toolkit. Może wyglądać jak Windows Commander (Total Commander ;)) lub
MS-Explorer przy czym jest prosty i szybki.

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
export FOX_CONFIG=%{_bindir}/fox16-config
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/no
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{pt_PT,pt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ABOUT-NLS AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xfa
%attr(755,root,root) %{_bindir}/xfe
%attr(755,root,root) %{_bindir}/xfi
%attr(755,root,root) %{_bindir}/xfp
%attr(755,root,root) %{_bindir}/xfw
%{_datadir}/%{name}
%{_desktopdir}/xf*.desktop
%{_mandir}/man1/xf*.1*
%{_iconsdir}/hicolor/48x48/apps/xf*.png
%{_iconsdir}/hicolor/48x48/apps/xf*.xpm
%{_iconsdir}/hicolor/scalable/apps/xf*.svg
%{_datadir}/polkit-1/actions/org.xfe.root.policy
