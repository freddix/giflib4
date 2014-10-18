Summary:	GIF-manipulation library
Name:		giflib4
Version:	4.1.6
Release:	1
License:	X Consortium-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/giflib/giflib-%{version}.tar.bz2
# Source0-md5:	7125644155ae6ad33dbc9fc15a14735f
URL:		http://sourceforge.net/projects/giflib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIF loading and saving shared library. This version uses LZW
compression (warning: patent/license issues in some countries).

%package devel
Summary:	GIF-manipulation library header files and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and headers needed for developing programs that use libgif
to load and save GIF image files.

%package progs
Summary:	Programs for converting and transforming GIF images
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
This package contains various programs for manipulating GIF image
files.

%prep
%setup -qn giflib-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libgif.so.4
%attr(755,root,root) %{_libdir}/libgif.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgif.so
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

