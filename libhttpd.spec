Summary:	Hughes embedded webserver static library
Summary(pl.UTF-8):   Statyczna biblioteka osadzanego serwera WWW firmy Hughes
Name:		libhttpd
Version:	1.3
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.hughes.com.au/products/libhttpd/%{name}-1.3.tar.gz
# Source0-md5:	ea0fb523fdb467702d34185be55e940c
Patch0:		%{name}-persistent-e.patch
Patch1:		%{name}-cxx.patch
URL:		http://www.hughes.com.au/products/libhttpd/
BuildRequires:	autoconf
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hughes embedded webserver library with persistence and non-blocking
patches for daapd.

%description -l pl.UTF-8
Biblioteka osadzanego serwera WWW z utrzymywaniem połączeń i łatami
nieblokującymi dla daapd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install src/libhttpd.a $RPM_BUILD_ROOT%{_libdir}
install src/httpd.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/FAQ.txt doc/libhttpd.pdf README HISTORY
%{_libdir}/*
%{_includedir}/*
