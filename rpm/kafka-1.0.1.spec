%define install_dir /usr/apache/
%define kafka_dir kafka_2.11-1.0.1
%define _topdir /data/RPM/kafka/rpmbuild

Name:           kafka
Version:        1.0.1
Release:        %{getenv:BUILD_ID}%{?dist}
Summary:        Apache Kafka is a framework to enable, monitor and manage comprehensive data security across the Hadoop platform.

Group:          Application/dp
License:        Apache
URL:            http://ranger.apache.org
Source0:        kafka_2.10-0.10.1.2-SNAPSHOT.tgz

BuildRoot:      %{_topdir}/BUILDROOT
#BuildRequires: maven
#Requires:      maven

%description
This is Kafka description.

%prep
%setup -q -n %{kafka_dir}

%build
echo "building..."

%install
rm -rf %{buildroot}%{install_dir}%{kafka_dir}/*
mkdir -p %{buildroot}%{install_dir}
cp -r ${RPM_BUILD_DIR}/%{kafka_dir} %{buildroot}%{install_dir}
ls -al %{buildroot}%{install_dir}
echo "%{buildroot}%{install_dir}/%{kafka_dir}"

%pre
if [ $1 == 1 ];then
        echo "First Install ..."
        user=kafka
        group=kafka

        #create group if not exists
        egrep "^$group" /etc/group >& /dev/null
        if [ $? -ne 0 ];then
                echo "add group kafka"
                groupadd $group
        fi

        #create user if not exists
        egrep "^$user" /etc/passwd >& /dev/null
        if [ $? -ne 0 ];then
                echo "add user kafka"
                useradd -g $group $user
        fi
fi

%post
ln -s %{install_dir}%{kafka_dir} %{install_dir}kafka

%files
%defattr (-,kafka,kafka,0755)
%{install_dir}/%{kafka_dir}/

%postun
echo "post uninstall  rm soft link..."
rm -rf %{install_dir}/kafka
exit 0

%doc

%changelog
*  Tue Sep 14 2017 qingfa.zhou <qingfa.zhou@wormpex.com> - 0.10.1
- First packaging Apache Kakfa.