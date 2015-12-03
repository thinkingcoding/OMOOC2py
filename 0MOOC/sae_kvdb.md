- sae-kvdb: API使用手册
		class sae.kvdb.Error
- 通用错误

		class sae.kvdb.Client(debug=0)
- debug 是否输出详细调试、错误信息到日志，默认关闭

		set(key, val, min_compress_len=0)
- 设置key的值为val

- 参数:	min_compress_len – 启用zlib.compress压缩val的最小长度，如果val的长度大于此值，则启用压缩，0表示不压缩。
		add(key, val, min_compress_len=0)
- 同set，但只在key不存在时起作用

		replace(key, val, min_compress_len=0)
- 同set，但只在key存在时起作用

		delete(key)
- 删除key。

		get(key)
- 从KVDB中获取一个key的值，存在返回key的值，不存在则返回None

		get_multi(keys, key_prefix='')
- 从KVDB中一次获取多个key的值。返回一个key/value的dict。
- 目前keys为一个字符串，当且仅当key_prefix取值为keys[0:-1]时，才返回有效value
- 参数:	
  - keys – key的列表，类型必须为list。
  - key_prefix – 所有key的前缀。请求时会在所有的key前面加上该前缀，返回值里所有的key都会去掉该前缀。

		get_by_prefix(prefix, limit=100, marker=None)
- 从KVDB中查找指定前缀的 key/value pair。返回一个generator，yield的item为一个(key, value)的tuple。
		generator = get_by_prefix(prefix)
		mylist = [i for i in generator] 
- 参数:	
  - prefix – 需要查找的key的前缀。
  - limit – 最多返回的item个数，默认为100。
  - marker – 指定从哪一个key开始继续查找，只返回该key后面的结果（该key不含在内）。

		getkeys_by_prefix(prefix, limit=100, marker=None)
- 从KVDB中查找指定前缀的key。返回符合条件的key的generator。
- 参数:	
  - prefix – 需要查找的key的前缀。
  - limit – 最多返回的key的个数，默认为100。
  - marker – 指定从哪一个key开始继续查找，只返回该key后面的结果（该key不含在内）。

		disconnect_all()
- 关闭KVDB连接