%include	/usr/lib/rpm/macros.perl
Summary:	IRC -> Onet Czat proxy
Summary(pl):	Proxy IRC -> Onet Czat
Name:		onetkonekt
Version:	1.0
Release:	0.1
License:	Beerware
Group:		Applications/Communications
Source0:	http://pld.toster.org/%{name}-%{version}.tar.gz
# Source0-md5:	0f759d99d3dd22cae8e8434895ecbe03
URL:		http://onetkonekt.apcoh.org/
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thanks to onetkonekt you can pick up chicks on Onet Czat servers using
your favourite IRC client.

%description -l pl
Dzi�ki temu programowi mo�na podrywa� cziki na czacie Onetu, u�ywaj�c
swojego ulubionego klienta IRC.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},/etc/{sysconfig,rc.d/init.d}}

install onetkonekt.pl $RPM_BUILD_ROOT%{_bindir}/onetkonekt.pl
install onet $RPM_BUILD_ROOT/etc/sysconfig/onet
install onet.conf $RPM_BUILD_ROOT%{_sysconfdir}/onet.conf
install onet.rc $RPM_BUILD_ROOT/etc/rc.d/init.d/onet

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add onet
if [ -f /var/lock/subsys/onet ]; then
	/etc/rc.d/init.d/onet restart >&2
else
	echo "Run \"/etc/rc.d/init.d/onet start\" to start onet daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/onet ]; then
		/etc/rc.d/init.d/onet stop >&2
	fi
	/sbin/chkconfig --del onet
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/onetkonekt.pl
%attr(754,root,root) /etc/rc.d/init.d/onet
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/onet
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/onet.conf
