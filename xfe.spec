Summary:	X File Explorer (Xfe) is a filemanager for X. 
Summary(pl):	X File Explorer (Xfe) is a filemanager for X. 
Name: 		xfe
Version:	0.54
Release: 	0.1
License: 	GPL
Group: 		Applications/File
Source: 	%{name}-%{version}.tar.gz
Requires: 	fox >= 1.0
BuildRequires: 	fox-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X File Explorer (Xfe) is a filemanager for X. 
It is based on the popular X Win Commander, which is
discontinued. Xfe is desktop independent and is 
written with the C++ Fox Toolkit. It has Windows Commander
or MS-Explorer look and is very fast and simple. 

%description -l pl
X File Explorer (Xfe) to mened¼er plików dla X'ów.
Jest oparty na popularnym X Win Commander, który nie jest ju¿
rozwijany. Xfe jest niezale¿ny od desktopu, jest napisany za
pomoc± C++ Fox Toolkit. Mo¿e wygl±daæ jak Windows Commander
(Total Commander ;)) lub MS-Explorer przy czym jest prosty i szybki.

%prep
%setup -q

%build
%configure \
	 --with-included-gettext \
	 --with-static=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

$find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO FAQ BUGS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/foxicons
%{_libdir}/foxrc
%{_pixmapsdir}/*
