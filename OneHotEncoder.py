def oneHotEncoder_process():
    service_list=['aol','auth','bgp','courier','csnet_ns','ctf','daytime','discard','domain','domain_u','echo','eco_i','ecr_i','efs','exec','finger','ftp','ftp_data','gopher','harvest','hostnames','http','http_2784','http_443','http_8001','imap4','IRC','iso_tsap','klogin','kshell','ldap','link','login','mtp','name','netbios_dgm','netbios_ns','netbios_ssn','netstat','nnsp','nntp','ntp_u','other','pm_dump','pop_2','pop_3','printer','private','red_i','remote_job','rje','shell','smtp','sql_net','ssh','sunrpc','supdup','systat','telnet','tftp_u','tim_i','time','urh_i','urp_i','uucp','uucp_path','vmnet','whois','X11','Z39_50']
    values = np.array(service_list)
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    #source_file = 'corrected_handled2.csv'
    #handled_file_onehot = 'corrected_handled_onehot.csv'
    # binary encode
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1) #调整为单列
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    print(onehot_encoded)
    return 
    #invert first example 反编译第一个样例
    inverted = label_encoder.inverse_transform([np.argmax(onehot_encoded[0, :])])
    print(inverted)
