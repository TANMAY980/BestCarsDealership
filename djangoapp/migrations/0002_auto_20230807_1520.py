# Generated by Django 3.1.3 on 2023-08-07 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='type',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='model_type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Wagon', 'Station wagon'), ('Sport', 'Sports Car'), ('Coupe', 'Coupe'), ('Mini', 'Mini van'), ('Van', 'Van'), ('Pickup', 'Pick-up truck'), ('Truck', 'Truck'), ('Bike', 'Motor bike'), ('Scooter', 'Scooter'), ('Other', 'Other')], default='Sedan', max_length=15),
        ),
        migrations.AlterField(
            model_name='carmake',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='carmake',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='car_make',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='dealer_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(choices=[(1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023, verbose_name='year'),
        ),
    ]
