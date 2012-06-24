Summary:	Bing, a point-to-point bandwidth measurement tool (b from Bandwitch)
Summary(pl):	Bing, narz�dzie s�u��ce mierzeniu przepustowo�ci ��czy 
Name:		bing
Version:	1.0.4
Release:	1
License:	BSD
Group:		Net/Utilities
Group(pl):	Sie�/Narz�dzia
Source:		bing-1.0.4.tar.bz2
Patch:		bing.patch

#URL:		http://??? email:pb@fasterix.freenix.fr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#Buildarch:	noarch

%description
Bing determines the real (raw, as opposed to available or average)
throughput on a link by measuring ICMP echo requests roundtrip times
for different packet sizes for each end of the link.

%description -l pl
Bing oblicza aktualn� (w przeciwie�stwie do np. �redniej) przepustowow��
��cza mierz�c czasy powrotu odpowiedzi na komunikaty ICMP.

%prep 
rm -rf %{buildroot}
%setup 
%patch -p0 

%build
make

%install
install -d %{buildroot}/usr/bin/
install bing %{buildroot}/usr/bin/bing
gzip -9nf README bing.8 bing.ps ChangeLog
install bing.8.gz %{_mandir}/man8

%files
%defattr(755,bin,bin,755)
/usr/bin/bing
%doc {README,ChangeLog,bing.ps}.gz 
%{_mandir}/man8/bing.8.gz
