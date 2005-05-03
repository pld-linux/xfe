Summary:	X File Explorer (Xfe) is a filemanager for X
Summary(pl):	X File Explorer - zarz±dca plików dla X
Name:		xfe
Version:	0.80
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/xfe/%{name}-%{version}.tar.gz
# Source0-md5:	fc980b3ad44a2160d9289df1fabb09c4
URL:		http://roland65.free.fr/xfe/
BuildRequires:	automake
BuildRequires:	fox-devel >= 1.4
BuildRequires:	fox-devel < 1.5
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
Requires:	fox >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X File Explorer (Xfe) is a filemanager for X. It is based on the
popular X Win Commander, which is discontinued. Xfe is desktop
independent and is written with the C++ Fox Toolkit. It has Windows
Commander or MS-Explorer look and is very fast and simple.

%description -l pl
X File Explorer (Xfe) to zarz±dca plików dla systemu X Window. Jest
oparty na popularnym X Win Commander, który nie jest ju¿ rozwijany.
Xfe jest niezale¿ny od desktopu, jest napisany za pomoc± C++ Fox
Toolkit. Mo¿e wygl±daæ jak Windows Commander (Total Commander ;)) lub
MS-Explorer przy czym jest prosty i szybki.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/foxicons
%{_prefix}/lib/foxrc
%{_pixmapsdir}/*
%{_mandir}/man1/*
