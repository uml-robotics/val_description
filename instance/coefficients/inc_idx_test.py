import pysmt

inc_raw = pysmt.getResource("/neck/j2/IncEnc_IdxAng_Raw")
inc_enc_last = inc_raw()

while True:
    diff = inc_raw() - inc_enc_last
    inc_enc_last = inc_raw()
    if abs(diff) != 1668 and diff != 0:
        print "Diff: ", diff

