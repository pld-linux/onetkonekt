Summary:	IRC -> Onet Czat proxy
Summary(pl):	IRC -> Onet Czat proxy
Name:		onetkonekt
Version:	0.3
Release:	0.1
License:	Beerware
Group:		Applications/Communications
Source0:	http://krzynio.hakore.com/%{name}-%{version}.tar.gz
# Source0-md5:	a7ee88ddbfb117106c0a8e023168bb2e
URL:		http://onetkonekt.apcoh.org
PreReq:		rc-scripts
Requires:	perl-modules
Requires(post,preun):	/sbin/chkconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thanks to onetkonekt you can pick up chicks on Onet Czat servers using
your favourite IRC client.

%description -l pl
Dziêki temu programowi mo¿na podrywaæ cziki na czacie Onetu, u¿ywaj±c
swojego ulubionego klienta IRC.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/etc/sysconfig/
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d/
install -d $RPM_BUILD_ROOT%{_sysconfdir}

install onetkonekt.pl $RPM_BUILD_ROOT%{_bindir}/onetkonekt.pl
install onet $RPM_BUILD_ROOT/etc/sysconfig/onet
install onet.conf $RPM_BUILD_ROOT%{_sysconfdir}/onet.conf
install onet.rc $RPM_BUILD_ROOT/etc/rc.d/init.d/onet

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/onetkonekt.pl
%attr(754,root,root) /etc/rc.d/init.d/onet
%defattr(644,root,root,755)
%config(noreplace) /etc/sysconfig/onet
%config(noreplace) %{_sysconfdir}/onet.conf


%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/chkconfig --add onet
echo "Run \"/etc/rc.d/init.d/onet start\" to start onet daemon."

%preun
/sbin/chkconfig --del onet
