Name: python
Version: 3.1.3
Summary: Version 3 of the Python programming language aka Python 3000
License: Python
URL: http://www.python.org/
Source: http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2

BuildRequires: library/readline
BuildRequires: library/ncurses
BuildRequires: library/security/openssl
BuildRequires: library/zlib
BuildRequires: library/expat

Requires: library/expat
Requires: library/security/openssl
Requires: library/zlib

%description
Python 3 is a new version of the language that is incompatible with the 2.x line of releases. The language is mostly the same, but many details, especially how built-in objects like dictionaries and strings work, have changed considerably, and a lot of deprecated features have finally been removed.

%prep
%setup -q -n Python-%{version}

%build
./configure --prefix=%{_prefix} \
            --enable-shared \
            --with-threads \
            --with-computed-gotos \
            --enable-ipv6 \
            --with-wide-unicode \
            --with-system-expat

make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

ln -sf python3 $RPM_BUILD_ROOT%{_bindir}/python
ln -sf python3-config $RPM_BUILD_ROOT%{_bindir}/python-config
ln -sf idle3 $RPM_BUILD_ROOT%{_bindir}/idle
ln -sf pydoc3 $RPM_BUILD_ROOT%{_bindir}/pydoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_mandir}/*
