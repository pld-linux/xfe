Summary:	X File Explorer (Xfe) is a filemanager for X
Summary(pl):	X File Explorer - zarz±dca plików dla X
Name:		xfe
Version:	0.54.2
Release:	0.1
License:	GPL
Group:		Applications/File
Source0:	http://dl.sourceforge.net/xfe/%{name}-%{version}.tar.gz
# Source0-md5:	4d50faa3153cd1ff4e9f4237926f44b1
URL:		http://www.roland65.ovh.org/xfe/xfe.html
BuildRequires:	fox-devel >= 1.0
Requires:	fox >= 1.0
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
%configure \
	 --with-included-gettext \
	 --with-static=no

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
%doc AUTHORS README TODO FAQ BUGS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/foxicons
%{_libdir}/foxrc
%{_pixmapsdir}/*
%{_mandir}/man1/*
