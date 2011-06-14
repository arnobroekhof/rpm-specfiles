Summary	: Install ruby 1.8.7
Name		: ruby
Version		: 1.8.7
Release		: p334
License		: BSD
Group		: Applications
Source0 	: ruby-1.8.7-p334.tar.gz
BuildArch	: x86_64
BuildRoot	: /var/tmp/%{name}-buildroot
BuildRequires	: openssl, openssl-devel, gcc, zlib, zlib-devel, make
Prereq      	: /sbin/chkconfig, /bin/cp, /bin/mv
Prereq      	: sh-utils, textutils, /usr/sbin/groupadd, /usr/sbin/useradd

%description
Ruby is a dynamic, reflective, general-purpose object-oriented programming language that combines syntax inspired by Perl with Smalltalk-like features. Ruby originated in Japan during the mid-1990s and was first developed and designed by Yukihiro "Matz" Matsumoto. It was influenced primarily by Perl, Smalltalk, Eiffel, and Lisp.

%prep
%setup

%build
./configure \
	--enable-pthread \
	--libdir=/usr/lib/ruby \
	--bindir=/usr/bin \
	--sbindir=/usr/sbin
%{__make}


%pre


%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}" \
	INSTALL_OPTS="" \
	COMMAND_OPTS="" \
	INIT_OPTS=""
%{__install} -d -m0755 %{buildroot}/usr/lib/ruby


%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
/usr/lib/ruby
/usr/bin/ruby
/usr/bin/erb
/usr/bin/irb
/usr/bin/rdoc
/usr/bin/ri
/usr/bin/testrb
/usr/local/share/man/man1/ruby.1

%post

%preun

%changelog
* Mon Jun 14 2011 Arno Broekhof <arnobroekhof@gmail.com>
- Initial spec-file
